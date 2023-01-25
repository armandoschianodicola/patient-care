var ingredient_list = document.getElementById("ingredient-list");
var add_fields = document.getElementById("add-field");
var remove_fields = document.getElementById("remove-field");
var calculate_fields = document.getElementById("calculate");
const mydata = JSON.parse(document.getElementById('mydata').textContent);

add_fields.onclick = function () {
  var newDiv = document.createElement("div");
  var newFieldText = document.createElement("input");
  var newFieldNum = document.createElement("input");

  newDiv.setAttribute('class', 'form-row d-flex justify-content-between');

  attrs = {
    type: "text",
    name: "ingredient[]",
    placeholder: "Aggiungi ingrediente",
    class: "form-group col-md-4 autocomplete",
  };
  for (attr in attrs) {
    newFieldText.setAttribute(attr, attrs[attr]);
  }
  attrs = {
    type: "number",
    name: "ingredient[]",
    placeholder: "Aggiunti Quantità",
    class: "form-group col-md-4 autocomplete",
  };
  for (attr in attrs) {
    newFieldNum.setAttribute(attr, attrs[attr]);
  }
  newDiv.appendChild(newFieldText);
  newDiv.appendChild(newFieldNum);
  ingredient_list.appendChild(newDiv);
};

remove_fields.onclick = function () {
  var input_fields = ingredient_list.getElementsByClassName("autocomplete");
    ingredient_list.removeChild(input_fields[input_fields.length - 1]);
};

calculate_fields.onclick = function () {
  var input_fields = ingredient_list.getElementsByClassName("autocomplete");
    ;
};
