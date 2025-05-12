(function(){

    async function fetchWithRetry(url, options = {}, retries = 3, delayMs = 2000) {
        let delay = (ms) => new Promise(res => setTimeout(res, ms)); // Delay function
    
        for (let attempt = 1; attempt <= retries; attempt++) {
            try {
                const response = await fetch(url, options);
                
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
    
                return await response.json(); // Return the JSON response if successful
    
            } catch (error) {
                if (attempt < retries) {
                    await delay(delayMs * attempt); // Exponential backoff (1s, 2s, 3s...)
                } else {
                    throw new Error("Request failed after multiple attempts");
                }
            }
        }
    }
    
    document.addEventListener('alpine:init', () => {
        Alpine.data('inquiryForm', () => ({
            init() {
                this.populateProducts()
                this.populateDoctors()
            },
            submissionLoading: false,
            submissionNumber: null,
            stepNumber: userId ? 3 : 1,
            stepCount: 6,
            stepName() {
                return {
                    1: "Persönliche Daten",
                    2: "Einwilligung",
                    3: "Anfrage senden",
                    4: "Kaution bezahlen"
                }[this.stepNumber]
            },
            symptomOptions: [
                "AD(H)S",
                "Depression",
                "Hauterkrankung",
                "Schlafstörung",
                "Krebserkrankung",
                "Angststörung / PTBS",
                "Chronische Schmerzen",
                "Migräne / Kopfschmerzen",
            ],
            products: [],
            productSearchFilter: "",
            newProductName: "",
            populateProducts: async function() {
                try {
                    const data = await fetchWithRetry('/api/v1/products/');
                    this.products = data
                } catch (error) {
                    this.products = [];
                }
            },
            filterProducts: function (products) {
                const wordsToInclude = this.productSearchFilter.split(" ")
                const includesAllWords = function(name) {
                    let valid = true
                    wordsToInclude.forEach((word) => {
                        if (!name.toLowerCase().includes(word.toLowerCase())){
                            valid = false
                        }
                    })
                    return valid
                }
                return products.filter((n) => includesAllWords(n)).filter((p) => !this.formValues.medication_wish.map((p) => p.name).includes(p))
            },
            addProduct: function (name) {
                this.formValues.medication_wish.push({
                    "name": name,
                    "quantity": 5
                })
                this.productSearchFilter = ""
                this.wantsNewProduct = false
            },
            addProductCustom: function (){
                this.formValues.medication_wish.push({
                    "name": this.newProductName,
                    "quantity": 5
                })
                this.newProductName = ""
                this.wantsNewProduct = false
            },
            removeProduct: function (product) {
                this.formValues.medication_wish = this.formValues.medication_wish.filter((p) => p.name !== product)
            },
            setQuantity: function (name, quantity) {
                // where the "name" is name, replace the quantity with the new quantity
                this.formValues.medication_wish = this.formValues.medication_wish.map((p) => {
                    return {
                        name: p.name,
                        quantity: name === p.name ? quantity : p.quantity
                    }
                })
            },
            wantsNewProduct: false,
            get showSelectProductDropdown() {
                return this.formValues.medication_wish.length === 0 || this.wantsNewProduct
            },
            doctorOptions: [],
            populateDoctors: async function() {
                try {
                    const data = await fetchWithRetry('/api/v1/doctors/', {}, 3, 1000);
                    this.doctorOptions = data
                } catch (error) {
                    this.doctorOptions = [{
                        id: 2,
                        name: "Dr. Rea Bitansky"
                    }];
                }
            },
            symptomDurationOptions: [
                "unter 3 Monate",
                "3-6 Monate",
                "über 6 Monate",
            ],
            exclusionCriteria: [
                "Schizophrenie, Wahnvorstellungen, Halluzinationen oder andere Zeichen einer Psychose",
                "Suchterkrankungen wie Alkoholismus oder andere Drogenabhängigkeit",
                "Herzinsuffizenz, Koronare Herzkrankheit, Herzrhythmusstörungen oder vorheriger Herzinfakt, Schlaganfall oder Thrombose / Embolie",
                "Allergie gegen THC/CBD-haltige Produkte",
                "Schwangerschaft bzw. Stillzeit",
                "innerhalb der letzten 30 Tage 100.000 mg Cannabis als getrocknete Blüten oder 1.000 mg Cannabisextrakt (THC-Gehalt) bezogen"
            ],
            formValues: {
                full_name: 'Gab Mar',
                birth_date: '2002-10-10',
                address: 'Teststreet',
                zip_code: '434343',
                city: 'Offenbach',
                phone: '231323232323232',
                email: 'gabri.marcan@gmail.com',
                checkbox_withdrawal: true,
                checkbox_communication: true,
                checkbox_data_sharing: true,
                checkbox_data_policy: true,
                checkbox_newsletter: true,

                symptoms: ["AD(H)S"],
                symptom_text: 'Lots more',
                symptom_severity: 6,
                symptom_duration: '3-6 Monate',
                was_already_treated: 'Ja',
                agreed_no_exclusion_criteria: true,
                previously_taken_medication: 'Ja',
                previous_medication_details: 'Citaloprame 15mg',
                previously_taken_cannabis: 'No',
                previous_cannabis_details: 'No cannabis experience',
                doctor_wish: 2,
                medication_wish: [{
                    "name": "Testprod",
                    "quantity": 10
                }]
                // full_name: '',
                // birth_date: '',
                // address: '',
                // zip_code: '',
                // city: '',
                // phone: '',
                // email: '',
                // checkbox_withdrawal: false,
                // checkbox_communication: false,
                // checkbox_data_sharing: false,
                // checkbox_data_policy: false,
                // checkbox_newsletter: false,

                // symptoms: [],
                // symptom_text: '',
                // symptom_severity: 1,
                // symptom_duration: '',
                // was_already_treated: null,
                // agreed_no_exclusion_criteria: false,
                // previously_taken_medication: '',
                // previous_medication_details: '',
                // previously_taken_cannabis: '',
                // previous_cannabis_details: '',
                // doctor_wish: '',
                // medication_wish: []
            },
            get isAdult() {
                if (!this.formValues.birth_date) return true

                const birthDate = new Date(this.formValues.birth_date)
                const today = new Date()
                const age = today.getFullYear() - birthDate.getFullYear()
                const month = today.getMonth() - birthDate.getMonth()
                if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
                    return age - 1 > 18
                }
                return age >= 18
            },
            get isTreatmentPossible() {
                if (!this.formValues.symptom_duration) return true

                if (this.formValues.symptom_duration === "unter 3 Monate"){
                    return false
                }
                if (this.formValues.symptom_severity < 6){
                    return false
                }

                return true
            },
            get maximumQuantityExceeded() {
                return this.formValues.medication_wish.reduce((acc, curr) => acc + parseInt(curr.quantity), 0) > 100
            },
            isValidUntilStep(step) {
                // The user can't go back to entering their personal details and changing the checkboxes
                // when they have clicked the continuing link in the email
                if (step < 2 && userId) return false

                // When the user saw the "check your email" screen, don't allow them to go further into the form
                if (step >= 3 && !userId) return false

                switch(step){
                    case 0:
                        return true
                    case 1:
                        const validateEmail = (email) => {
                            return String(email)
                                .toLowerCase()
                                .match(
                                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                                );
                        };
                        let filled = ['full_name', 'birth_date', 'address', 'zip_code', 'city', 'phone', 'email'].every(field => this.formValues[field])
                        let validEmail = validateEmail(this.formValues.email)
                        let validPhone = this.formValues.phone.length >= 8
                        return filled && validEmail && validPhone && this.isAdult
                    case 2:
                        return ['checkbox_withdrawal', 'checkbox_communication', 'checkbox_data_sharing', 'checkbox_data_policy'].every(field => this.formValues[field])  
                    case 3:
                        const filledOut = ['symptoms', 'symptom_text', 'symptom_duration', 'was_already_treated'].every(field => this.formValues[field])
                        return filledOut && this.isTreatmentPossible && this.formValues.symptom_text.length >= 50
                    case 4:
                        return this.formValues["agreed_no_exclusion_criteria"]
                    case 5:
                        if (this.formValues["previously_taken_medication"] === '') return false

                        const filledOutCannabis = this.formValues["previously_taken_cannabis"] && this.formValues["previous_cannabis_details"]

                        if (this.formValues["previously_taken_medication"] === 'Ja'){
                            return filledOutCannabis && this.formValues["previous_medication_details"]
                        }

                        return filledOutCannabis
                    case 6:
                        return this.formValues.doctor_wish && this.formValues.medication_wish.length > 0 && !this.maximumQuantityExceeded
                }
            },
            get isFormValid() {
                return this.isValidUntilStep(this.stepNumber)
            },
            toggleSymptom(option) {
                var index = this.formValues.symptoms.indexOf(option);

                if (index === -1) {
                    this.formValues.symptoms.push(option);
                } else {
                    this.formValues.symptoms.splice(index, 1);
                }
            },
            selectDoctor(doctor) {
                this.formValues.doctor_wish = doctor
            },
            gotoPage (page) {
                if (!this.isValidUntilStep(page - 1)) return
                this.stepNumber = page
                window.scrollTo({ top: 0, behavior: 'smooth' })
            },
            clickedNext() {
                const that = this

                async function submitForm(data) {
                    that.submissionLoading = true
                    const rawResponse = fetch('/api/v1/submit-form/', {
                        method: 'POST',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'X-CSRFTOKEN': csrfToken
                        },
                        body: JSON.stringify(data)
                    }).then(response => {
                        if (response.ok) {
                            response.json().then((data) => {
                                that.submissionNumber = data.number
                                that.submissionLoading = false
                            })
                          } else {
                            that.submissionLoading = false
                            alert("Leider gab es einen Fehler. Bitte versuche es erneut. Falls das Problem bestehen bleibt, kontaktiere bitte unseren Support unter info@medicanova.de")
                            throw new Error("Failed to fetch", {response});  
                          }
                    }).catch((error) => console.log(error));
                }

                async function createOrUpdateUser(data) {
                    that.submissionLoading = true
                    const rawResponse = fetch('/api/v1/users/', {
                        method: 'POST',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'X-CSRFTOKEN': csrfToken
                        },
                        body: JSON.stringify(data)
                    }).then(response => {
                        if (response.ok) {
                            response.json().then((data) => {
                                that.submissionLoading = false
                            })
                          } else {
                            that.submissionLoading = false
                            alert("Leider gab es einen Fehler. Bitte versuche es erneut. Falls das Problem bestehen bleibt, kontaktiere bitte unseren Support unter info@medicanova.de")
                            throw new Error("Failed to fetch", {response});  
                          }
                    }).catch((error) => console.log(error));
                }

                if (!this.isFormValid) return

                if (this.stepNumber === 2){
                    // Submitted personal details – create a user
                    createOrUpdateUser({
                        role: "patient",
                        username: this.formValues.email,
                        email: this.formValues.email,
                        full_name: this.formValues.full_name,
                        birth_date: this.formValues.birth_date,
                        address: this.formValues.address,
                        zip_code: this.formValues.zip_code,
                        city: this.formValues.city,
                        phone: this.formValues.phone,

                        checkbox_honesty: this.formValues.checkbox_honesty,
                        checkbox_data_sharing: this.formValues.checkbox_data_sharing,
                        checkbox_data_policy: this.formValues.checkbox_data_policy,
                        checkbox_newsletter: this.formValues.checkbox_newsletter
                    })
                }

                if (this.stepNumber >= this.stepCount){
                    submitForm({
                        user_id: userId,
                        ...this.formValues,
                        was_already_treated: this.formValues.was_already_treated === 'Ja',
                        previously_taken_medication: this.formValues.previously_taken_medication === 'Ja',
                        previously_taken_cannabis: this.formValues.previously_taken_cannabis === 'Ja'
                    })
                    return
                }

                this.stepNumber += 1
                window.scrollTo({ top: 0, behavior: 'smooth' })
            },
            clickedPrevious() {
                if (this.stepNumber === 1) return

                // The user can't go back to entering their personal details and changing the checkboxes
                // when they have clicked the continuing link in the email
                if (userId && this.stepNumber <= 3) return

                this.stepNumber -= 1
                window.scrollTo({ top: 0, behavior: 'smooth' })
            },
        }))
    })
    

})()