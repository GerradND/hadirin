function showDropdownItems(e) {
    e.currentTarget.nextElementSibling.classList.toggle("show")
}

function hideDropdown(e) {
    if(e.relatedTarget !== null && e.relatedTarget.className === 'dropdown-item'){
        e.preventDefault();
    } else {
        e.currentTarget.nextElementSibling.classList.remove("show")
    }
}

const dropdownButton = document.querySelector('#dropdown-button')
dropdownButton.addEventListener('click', (e) => showDropdownItems(e))
dropdownButton.addEventListener('focusout', (e) => hideDropdown(e))