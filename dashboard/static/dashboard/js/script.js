(function(){

    document.addEventListener('alpine:init', () => {
        Alpine.data('dashboard', () => ({
            showSidebar: false,
        }))
    })

})()