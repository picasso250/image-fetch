<?php

require 'lib.php';


function fetch_url($url)
{
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $ret = curl_exec($ch);
    curl_close($ch);
    return $ret;
}

function fetch_page($page_url)
{
    $html = fetch_url($page_url);
    // echo $html;
    if (!preg_match_all('%<img src="([^"]+.douban.com/view/group_topic/large/public/p\d+.jpg)"%i', $html, $matches)) {
        echo "no image in this page\n";
        return false;
    }
    foreach ($matches[1] as $image_url) {
        $file_name = substr($image_url, strrpos($image_url, '/')+1);
        $file_name = __DIR__.'/images/'.$file_name;
        if (is_file($file_name)) {
            echo "skip $file_name\n";
            continue;
        }
        echo "save $file_name \n";
        image_save($file_name, $image_url);
    }
    return count($matches[1]);
}

$group_root = 'http://www.douban.com/group/haixiuzu/';
$html = fetch_url($group_root);
// echo $html;
if (!preg_match_all('%<a href="(http://www.douban.com/group/topic/\d+/)"%i', $html, $matches)) {
    throw new Exception("no link for group topic", 1);
}
foreach ($matches[1] as $topic_url) {
    echo "fetch topic $topic_url\n";
    fetch_page($topic_url);
}
