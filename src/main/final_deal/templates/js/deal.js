<script type="text/javascript">
		function showdiv(){
			var val = event.target.options[event.target.selectedIndex].value;
			if ((val === "25%-25%-50%") || (val === "33%-33%-33%") || (val === "40%-20%-40%")){
				console.log("yes");
				document.getElementById("row1").style.display = "flex";
				document.getElementById("row2").style.display = "flex";
				document.getElementById("row3").style.display = "flex";
				document.getElementById("row4").style.display = "flex";


			}
			if (val === "50%-50%")
			{
				console.log("yessssss!!!!");
				document.getElementById("row1").style.display = "flex";
				document.getElementById("row2").style.display = "flex";
				document.getElementById('row3').style.display = "none";
				document.getElementById("row4").style.display = "flex";
			}
		}
		function OnChangeCheckbox (checkbox) {
            if (checkbox.checked) {
                // alert ("The check box is checked.");
                document.getElementById("other_dis1").style.display = 'flex';
                document.getElementById("other_dis2").style.display = 'flex';
                document.getElementById("other_dis3").style.display = 'flex';
            }
            else {
                // alert ("The check box is not checked.");
                 document.getElementById("other_dis1").style.display = 'none';
                document.getElementById("other_dis2").style.display = 'none';
                document.getElementById("other_dis2").style.display = 'none';
            }
        }
        function calculate1 (){
        	var box1 = document.getElementById('fct1').value;
        	
        	var box2 = document.getElementById('er1').value;
        	
        	var result = document.getElementById('a_fct1');
        	var mul1 = (box1/10) * box2;
        	
        	result.value = mul1;

        }
        function calculate2 (){
        	var box21 = document.getElementById('fct2').value;
        	
        	var box22 = document.getElementById('er2').value;
        	
        	var result1 = document.getElementById('a_fct2');
        	var mul21 = (box21/10) * box22;
        	
        	result1.value = mul21;

        }
        function calculate3 (){
        	var box31 = document.getElementById('fct3').value;
        	
        	var box32 = document.getElementById('er3').value;
        	
        	var result2 = document.getElementById('a_fct3');
        	var mul31 = (box31/10) * box32;
        	
        	result2.value = mul31;

        }
        function sum(){
        	// var num1 = parseInt(document.getElementById('a_fct1').value);
        	// var num2 = parseInt(document.getElementById('a_fct2').value);
        	// var num3 = document.getElementById('a_fct3').value;
        	// var add = num1 + num2 + num3;
        	// console.log("i am in");
        	// console.log(add);
        	// document.getElementById('totalbox').value = add;
        	var first_number = parseInt(document.getElementById("a_fct1").value);
            var second_number = parseInt(document.getElementById("a_fct2").value);
            var third_number = parseInt(document.getElementById("a_fct3").value);
            var result = first_number + second_number + third_number;
 
            document.getElementById("totalbox").value = result;
        }

	</script>