<?php

function image_save($name, $url)
{
    if (is_file($name)) {
        return false;
    }
    return file_put_contents($name, file_get_contents($url));
}
