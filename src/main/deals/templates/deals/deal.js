

    function calculate1(){
      var freq = document.getElementById('freq').value;
      console.log(freq)
    
      var result = document.getElementById('id_total_sec');
      var t1 = freq*10;
      console.log(t1,"---------")
      
      result.value = t1;
    }

    function calculate2(){
      var freq1 = document.getElementById('freq1').value;
      console.log(freq1)
    
      var result = document.getElementById('id_total_sec1');
      var t1 = freq1*10;
      console.log(t1,"---------")
      
      result.value = t1;
    }

    function total1(){
      var effrate = document.getElementById('er').value;
      var ts = document.getElementById('id_total_sec').value;
      var result = document.getElementById('total_cost');
      var t1 = (effrate*ts)/10;
      console.log(t1,"---------")
      
      result.value = t1;
    }

    function total2(){
      var effrate = document.getElementById('er1').value;
      var ts = document.getElementById('id_total_sec1').value;
      var result = document.getElementById('total_cost1');
      var t1 = (effrate*ts)/10;
      console.log(t1,"---------")
      
      result.value = t1;
    }

    function total3(){
      var effrate = document.getElementById('er2').value;
      var result = document.getElementById('total_cost2');
      // var t1 = (effrate*ts)/10;
      // console.log(t1,"---------")
      
      // result.value = t1;
    }

    function total4(){
      var effrate = document.getElementById('er3').value;
      var result = document.getElementById('total_cost3');
      // var t1 = (effrate*ts)/10;
      // console.log(t1,"---------")
      
      // result.value = t1;
    }

    function total5(){
      var effrate = document.getElementById('er4').value;
      var result = document.getElementById('total_cost4');
      // var t1 = (effrate*ts)/10;
      // console.log(t1,"---------")
      
      // result.value = t1;
    }

    function total6(){
      var effrate = document.getElementById('er5').value;
      var result = document.getElementById('total_cost5');
      // var t1 = (effrate*ts)/10;
      // console.log(t1,"---------")
      
      // result.value = t1;
    }

      function OnChangeCheckbox1 (checkbox) {
          if (checkbox.checked) {
              // alert ("The check box is checked.");
              document.getElementById("aston").style.display = 'block';
              var abc = document.getElementById("aston1")
              console.log(abc.getAttribute('id'))
              if (abc.checked==true){
                console.log("-------------",abc.checked)
              }
          }
          else {
              // alert ("The check box is not checked.");
               document.getElementById("aston").style.display = 'none';
          }
      }

        function OnChangeCheckbox2 (checkbox) {
            if (checkbox.checked) {
                // alert ("The check box is checked.");
                document.getElementById("lband").style.display = 'block';
                var abc = document.getElementById("lband1")
                console.log(abc.getAttribute('id'))
                if (abc.checked==true){
                console.log("-------------",abc.checked)
              }
            }
            else {
                // alert ("The check box is not checked.");
                 document.getElementById("lband").style.display = 'none';
            }
        }

        function OnChangeCheckbox3 (checkbox) {
            if (checkbox.checked) {
                // alert ("The check box is checked.");
                document.getElementById("logobug").style.display = 'block';
            }
            else {
                // alert ("The check box is not checked.");
                 document.getElementById("logobug").style.display = 'none';
            }
        }

        function OnChangeCheckbox4 (checkbox) {
            if (checkbox.checked) {
                // alert ("The check box is checked.");
                document.getElementById("sponsorshiptag").style.display = 'block';
            }
            else {
                // alert ("The check box is not checked.");
                 document.getElementById("sponsorshiptag").style.display = 'none';
            }
        }

        function OnChangeCheckbox5 (checkbox) {
            if (checkbox.checked) {
                // alert ("The check box is checked.");
                document.getElementById("ticker").style.display = 'block';
            }
            else {
                // alert ("The check box is not checked.");
                 document.getElementById("ticker").style.display = 'none';
            }
        }

        function OnChangeCheckbox6 (checkbox) {
            if (checkbox.checked) {
                // alert ("The check box is checked.");
                document.getElementById("wheatherbranding").style.display = 'block';
            }
            else {
                // alert ("The check box is not checked.");
                 document.getElementById("wheatherbranding").style.display = 'none';
            }
        }

      var trial ;             // global variable for storing channel
      $("#aston1").change(function () {
        
        trial = $(this).attr('id');
        console.log(trial)        // storing selected channel in trial variable
      });

      $("#id_channel_choice").change(function () {
        var url1 = $("#nonfct_form").attr("url");  // storing url....telling ajax to follow                          specified url
        var chan = $(this).val();   // storing the channel selected from row1
        
        
        $.ajax({
                               // initialize an AJAX request
        url: url1,                    // set the url of the request (= localhost:8000/hr/ajax/                    load-br/)
        data: {
          'checkbox1': trial , 'channel' :chan      // add the channel and band to the GET                          parameters by default it is GET method
        },

        success: function (data) {   // `data` is the return of the `load_br` view function
         
        var multiidhtml = $(data);
        var multiid = multiidhtml.find('#br1').attr("value"); // prints base rate in input type
        console.log(multiid);
              $("#br1").val(multiid);     // replace the contents of the band1 input with the                   data that came from the server
          }
            
          });
        });
