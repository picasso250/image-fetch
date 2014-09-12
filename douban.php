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

function fetch_page($page_url, $pattern)
{
    $html = fetch_url($page_url);
    // echo $html;
    if (!preg_match_all($pattern, $html, $matches)) {
        throw new Exception("no img", 1);
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


fetch_page('http://www.douban.com/group/topic/62688497/', '%<img src="([^"]+.douban.com/view/group_topic/large/public/p\d+.jpg)"%i');

// file_get_contents('http://www.douban.com/group/topic/62688497/');
$url = 'http://www.douban.com/group/topic/62688497/';

// $ch = curl_init($url);
// curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36');
// curl_exec($ch);
// curl_close($ch);
