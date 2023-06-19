<?php
echo "
<html>
<head>
<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">
<meta name=\"viewport\" content=\"width=device-width\">
<link href=\"https://fonts.googleapis.com/css?family=Acme&display=swap\" rel=\"stylesheet\">
<title>/: SMS AND CALL BOMBER</title>
<style>
body{
    text-align:center;
    font-family: 'Acme', sans-serif;
}
.text{

    padding:5px;
   text-align:center;

}
.btn{
    padding:5px;
    background:#36D6DE;
    border-radius:10px;
    font-size:15px;
    cursor:pointer;
}
.loader {
  border: 16px solid #f3f3f3;
  border-radius: 50%;
  border-top: 16px solid black;
  border-bottom: 16px solid green;
  width: 120px;
  height: 120px;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 3s linear infinite;
}

@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
<h1>GMAIL SENDER</h1>
<b>Script By : MR. JARVIS</b><br><br>
<B><Font color='green'>[UPDATED]</font></b><br><br>



<center><script type=\"text/javascript\">(function() {var script=document.createElement(\"script\");script.type=\"text/javascript\";script.async =true;script.src=\"//telegram.im/widget-button/index.php?id=@mrjarvisyt\";document.getElementsByTagName(\"head\")[0].appendChild(script);})();</script>
<a href=\"https://telegram.im/@mrjarvisyt\" target=\"_blank\" class=\"telegramim_button telegramim_shadow telegramim_pulse\" style=\"font-size:20px;width:310px;background:#FF0007;box-shadow:1px 1px 5px #FF0007;color:#FFFFFF;border-radius:50px;\" title=\"\"><i></i> Join Our Telegram Channel<small><span class=\"telegramim_count\" data-for=\"@mrjarvisyt\">...</span> participants</small></a>
</center><hr>
";
$to = $_GET['to'];
$from = $_GET['from'];
$mail_subject = $_GET['subject'];
$mail_content = $_GET['message'];
$header ="From: $from"."\r\n";
$result = mail($to,$mail_subject,$mail_content,$header);
if ($result) {
echo "<center>Mail Sent.</center>";
}
else {
echo "<center>Mail Not Sent.</center>";
}
echo " <div class=\"footer\">
  <h4>Created By : TECHNO AADARSH</h4>
</div>
";