<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>SUROS Lab | web UI -- 2208</title>
    </head>
    <body>
        running web_dbAPI_test.php...<br />
        <?php
        $searchList = shell_exec('python web_dbAPI_main.py "風味館"');
        echo $searchList;
        ?>
    </body>
</html>



