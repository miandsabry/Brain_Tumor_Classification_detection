var table = document.getElementById('myTable');



for(var i = 1; i < table.rows.length; i++)
{
    table.rows[i].onclick = function()
    {
         //rIndex = this.rowIndex;
         document.getElementById("PatientId").value = this.cells[0].innerHTML;
         document.getElementById("PatientName").value = this.cells[1].innerHTML;
         document.getElementById("age").value = this.cells[2].innerHTML;
         document.getElementById("Gender").value = this.cells[3].innerHTML;
         document.getElementById("History").value = this.cells[4].innerHTML;
    };
}


function myFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        }
        else {
        tr[i].style.display = "none";
        }
    }
  }
}

