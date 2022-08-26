<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>SUROS Lab | web UI -- 2208</title>
    </head>
    <body>
        running web_dbAPI_test.php...<br />
        <br />
        <?php
        $iptSearch = '高鐵';    //input search key
        $pathPy = 'python web_dbAPI_main.py ';    //python file path with one space in the end
        $reList = exec ($pathPy.$iptSearch);    //execute cmd to run python
        $reList = iconv('big5', 'utf-8', $reList);    //transfer text encode
        ?>

        <button class="icon_search" type="button" name="go_search" id="searchBtn" onclick="testAlert(<?php echo $reList; ?>)"><img src="image/search_2208A.png" /></button>
        testTable(<?php echo $reList; ?>)
        <script>
            testList(<?php echo $reList; ?>);


            /*
            function get_input(inputStr){
                var keySC = inputStr

            }
            */

            function testTable(pyResult){
                var listArr = pyResult;    //get py list
                var recLen = listArr.length;    //get records length
                var listTable = document.querySelector(".list");
                var oneData = "";
                var oneRow = "";
                for (var i = 0; i < recLen-1 ; i++ ){
                    for (var j = 0; j < 3 ; j++ ){
                        var oneCell = "<li>" + listArr[i][j] + "</li>";
                        oneData += oneCell;
                    }
                    oneRow += oneData;
                }
                listTable.innerHTML = oneRow;
            }
            
           
            function testList(pyResult){
                var listArr = pyResult;
                document.write (listArr[0][2]);
            }



            function testAlert(pyResult){
                var listArr = pyResult;    //get py list
                alert(listArr);
            }           
        </script>
    </body>
</html>


<!--
/*
$reList = exec ('python web_dbAPI_main.py 高鐵');
$reList = iconv('big5', 'utf-8', $reList);
var_dump ($reList);
*/
-->
