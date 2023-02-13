// var ingredient_list = document.getElementById("ingredient-list");
// var add_fields = document.getElementById("add-field");
// var remove_fields = document.getElementById("remove-field");
// var calculate_fields = document.getElementById("calculate");
// const mydata = JSON.parse(document.getElementById('mydata').textContent);

// add_fields.onclick = function () {
//   var newDiv = document.createElement("div");
//   var newFieldText = document.createElement("input");
//   var newFieldNum = document.createElement("input");

//   newDiv.setAttribute('class', 'form-row d-flex justify-content-between');

//   attrs = {
//     type: "text",
//     name: "ingredient[]",
//     placeholder: "Aggiungi ingrediente",
//     class: "form-group col-md-4 autocomplete",
//   };
//   for (attr in attrs) {
//     newFieldText.setAttribute(attr, attrs[attr]);
//   }
//   attrs = {
//     type: "number",
//     name: "ingredient[]",
//     placeholder: "Aggiunti Quantità",
//     class: "form-group col-md-4 autocomplete",
//   };
//   for (attr in attrs) {
//     newFieldNum.setAttribute(attr, attrs[attr]);
//   }
//   newDiv.appendChild(newFieldText);
//   newDiv.appendChild(newFieldNum);
//   ingredient_list.appendChild(newDiv);
// };

// remove_fields.onclick = function () {
//   var input_fields = ingredient_list.getElementsByClassName("autocomplete");
//     ingredient_list.removeChild(input_fields[input_fields.length - 1]);
// };

let formRow = document.querySelectorAll(".form-row");
let container = document.querySelector("#form-container");
let addButton = document.querySelector("#add-form");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");
let calculate_button = document.querySelector("#calculate");

let formNum = formRow.length - 1;
addButton.addEventListener("click", addForm);

function addForm(e) {
  e.preventDefault();
  console.log('formRow', formRow)

  let newForm = formRow[0].cloneNode(true);
  console.log(newForm)
  // for (var i = 0; i < newForm.childNodes.length; i++) {
  //   newForm.childNodes[i].innerHTML = "";
  // }
  let formRegex = RegExp(`form-(\\d){1}-`, "g");

  formNum++;
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
  container.appendChild(newForm);
  console.log(calculate_button.parentNode)
  container.insertBefore(calculate_button, newForm);


  totalForms.setAttribute("value", `${formNum + 1}`);
}

calculate_button.onclick = function () {
  var input_fields = container.querySelectorAll("input[type=number]");

  var result = 0.0;
  for (let i = 0; i < input_fields.length; i++) {
    if (input_fields[i].value) {
      result += parseInt(input_fields[i].value);
    }
  }
  document.getElementById("result").value = result;
};
