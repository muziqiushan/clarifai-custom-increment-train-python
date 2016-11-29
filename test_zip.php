<?php
/***************************************************************************
 * 
 * Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file test_zip.php
 * @author liyue06(liyue06@baidu.com)
 * @date 2016/07/10 15:17:31
 * @brief 
 *  
 **/
$zip = new ZipArchive();
$res = $zip->open("test.zip", ZipArchive::CREATE);
$zip->addFile("User.php");
$zip->close();
var_dump($res);exit;





/* vim: set expandtab ts=4 sw=4 sts=4 tw=80: */
