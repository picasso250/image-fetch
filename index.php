<?php

$attitude_map = json_decode(file_get_contents('attitude.json'), true);

/* AJAX check  */
if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    /* special ajax here */
    $action = $_POST['action'][0];
    $file = $_POST['file'];
    $attitude_map[$file] = $action;
    file_put_contents('attitude.json', json_encode($attitude_map));
    error_log("$action $file\n", 3, 'show.log');
    die(json_encode(array('code' => 0)));
}

$d = dir("images");
include 'head.html';
echo '<link rel="stylesheet" type="text/css" href="style.css">';
while (false !== ($entry = $d->read())) {
    $f = "images/$entry";
    $attitude = $attitude_map[$f];
    if (is_file($f) && $attitude === 'l') {
        include 'entry.html';
    }
}
$d->close();
