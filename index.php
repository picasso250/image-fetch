<?php

function get_data($name)
{
    return json_decode(file_get_contents($name.'.json'), true);
}

$attitude_map = get_data('attitude');

/* AJAX check  */
if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    /* special ajax here */
    $action = $_POST['action'][0];
    $file = $_POST['file'];
    $attitude_map[$file] = $action;
    if ($action === 'd') {
        unlink($file);
    }
    file_put_contents('attitude.json', json_encode($attitude_map));
    error_log("$action $file\n", 3, 'show.log');
    die(json_encode(array('code' => 0)));
}

$d = dir("images");
include 'head.html';
$image_page = get_data('image_page');
while (false !== ($entry = $d->read())) {
    $f = "images/$entry";
    $attitude = $attitude_map[$f];
    if (is_file($f) && $attitude !== 'd') {
        include 'entry.html';
    }
}
$d->close();
