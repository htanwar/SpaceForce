<?php
$servername = "";
$username = "";
$password = "";
$database = '';
$link = mysqli_connect($servername, $username, $password, $database);
// Check connection
if ($link === false) {
    die('ERROR: Could not connect. ' . mysqli_connect_error());
}
if(isset($_POST["username"])){
    $sql = "SELECT high_score FROM scores WHERE username = ?";

    if ($stmt = mysqli_prepare($link, $sql)) {
        // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, 's', $_POST["username"]);
        mysqli_stmt_bind_result($stmt, $score);

        // Attempt to execute the prepared statement
        if(mysqli_stmt_execute($stmt)){

            if(mysqli_stmt_fetch($stmt)){
                mysqli_stmt_close($stmt);

                json_encode ( $score );
                    echo intval($_POST["score"]) . intval($score);
                    if(intval($_POST["score"]) > intval($score)){

                        $sql2 = "UPDATE scores SET high_score = ? WHERE username = ?";

                        if ($stmt2 = mysqli_prepare($link, $sql2)) {

                            // Bind variables to the prepared statement as parameters
                            mysqli_stmt_bind_param($stmt2, 'is', $_POST["score"],$_POST["username"]);

                            // Attempt to execute the prepared statement
                            if (mysqli_stmt_execute($stmt2)) {

                            }
                            mysqli_stmt_close($stmt2);
                        }
                        else{
                            echo mysqli_error($stmt2);
                        }
                    }
            }
            else{
                $sql2 = "INSERT INTO scores (username, high_score) VALUES (?,?)";
                mysqli_stmt_close($stmt);

                if ($stmt2 = mysqli_prepare($link, $sql2)) {
                    // Bind variables to the prepared statement as parameters
                    mysqli_stmt_bind_param($stmt2, 'si', $_POST["username"],$_POST["score"]);

                    // Attempt to execute the prepared statement
                    if (mysqli_stmt_execute($stmt2)) {
                    }
                    mysqli_stmt_close($stmt2);

                }

            }
        }


        }

        else{

            echo "Error updating";
        }
    }
elseif (isset($_GET)){
    $sql = "SELECT username, high_score FROM scores ORDER BY high_score DESC";
    $result = mysqli_query($link, $sql);
    if ($stmt = mysqli_prepare($link, $sql)) {
        if(mysqli_num_rows($result) > 0)   // checking if there is any row in the resultset
        {
            $rank = 0;
            while($row = mysqli_fetch_assoc($result)){
                $rank += 1;
                if($row['username'] == $_GET['rank']){
                    echo $rank;
                    break;
                }
            }
        }

    }
}
else{
    $sql = "SELECT username, high_score FROM scores ORDER BY high_score DESC";
    $result = mysqli_query($link, $sql);
    if ($stmt = mysqli_prepare($link, $sql)) {
        if(mysqli_num_rows($result) > 0)   // checking if there is any row in the resultset
        {
            $rank = 0;
            while($row = mysqli_fetch_assoc($result)){
                $rank += 1;
                ?>
                        <div>
                            <p><?php echo $rank .'. ' . htmlspecialchars($row['username']) . ': ' . $row['high_score']; ?></p>

                        </div>
                <?php
            }
        }

    }
}
$link->close();
