// find selected checkboxes



var values = [];
var checkboxes_input = document.querySelectorAll('input[type=checkbox]');
var checkboxes_text = document.querySelectorAll('.custom-control-label');

// match the checkboxes with the labels
checkboxes_input.forEach((checkbox, index) => {
    checkbox.text = checkboxes_text[index].innerText;
    console.log(checkbox.text);
});

// add event listener to the checkboxes
checkboxes_input.forEach((checkbox,index) => {
    checkbox.addEventListener('change', (event) => {
        // get the values of the selected checkboxes
        values = [];
        if (checkbox.checked) {
            checkboxes_input.forEach((checkbox, index) => {
                if (checkbox.checked) {
                    values.push(checkbox.text);
                }
            });
        }
        console.log(values);
    });
});



console.log(categories);

