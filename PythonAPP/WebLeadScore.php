<html>
    <body>
        <form action="" method="post">
        To get LEAD SCOR please insert JSON file:
            <input type=text name="t1">

            <input type=submit name="s">
            <br><br><br>
            <?php

if(isset($_POST['s']))
{
    $a=$_POST['t1']; //accessing value from the text field
    while(!isset($a)){
    }
    $deletefile=unlink('data.json');
    $fp = fopen('data.json', 'a');
    fwrite($fp, $a);
    fclose($fp);
    // echo should happen only after 'while' condition changed 
    if (isset($a)){
    #echo "the score is: ";
    $command = escapeshellcmd('py GetScore.py');
    $output = shell_exec($command);
    while($output == null){ // idk if the default value is null check that please
        //do nothing
    }
    // echo should happen only after 'while' condition changed 
    echo "\n\n";
    echo $output;
    echo '%';
}
    

}

?>

        </form>
    </body>
</html>