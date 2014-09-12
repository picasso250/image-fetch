<?php

function image_save($name, $url)
{
    return file_put_contents($name, file_get_contents($url));
}

function fetch_page($page_url)
{
    $html = file_get_contents($page_url);
    // echo $html;
    if (!preg_match_all('/<img src2="([^"]+?)"/i', $html, $matches)) {
        throw new Exception("no img", 1);
    }
    foreach ($matches[1] as $image_url) {
        $file_name = substr($image_url, strrpos($image_url, '/')+1);
        echo "save $file_name \n";
        image_save($file_name, $image_url);
    }
    return count($matches[1]);
}
$page_url = 'http://www.moko.cc/post/1031624.html';

$root = 'http://www.moko.cc/';
$html = file_get_contents($root);
if (!preg_match_all('%<a href="/(post/\d+.html)"%i', $html, $matches)) {
    throw new Exception("no link to page", 1);
}
foreach ($matches[1] as $link) {
    $link = $root.$link;
    echo "fetch $link\n";
    fetch_page($link);
}
