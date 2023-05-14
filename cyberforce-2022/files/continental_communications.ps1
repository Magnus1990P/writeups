$wsh = New-Object -ComObject WScript.Shell
#$wsh.SendKeys("{CAPSLOCK}")

$init = "0101010"
$init = $init.ToCharArray();


## ENCODER - START
$encode = @{};
$encode["a"] = "1011"
$encode["b"] =""
$encode["c"] =""
$encode["e"] = ""
$encode["f"] = ""
$encode["g"] = ""
$encode["h"] = ""
$encode["i"] = ""
$encode["j"] = ""
$encode["k"] = ""
$encode["l"] = ""
$encode["m"] = ""
$encode["n"] = ""
$encode["o"] = ""
$encode["p"] = ""
$encode["q"] = ""
$encode["r"] = ""
$encode["s"] = ""
$encode["t"] = ""
$encode["u"] = ""
$encode["v"] = ""
$encode["w"] = ""
$encode["x"] = ""
$encode["y"] = ""
$encode["z"] = ""

$encode["1"] = "101101101"
$encode["2"] = "1010110101"
$encode["3"] = "1010101101"
$encode["4"] = "1010101011"
$encode["5"] = "11011011"
$encode["6"] = "10101010101"
$encode["7"] = "110110101"
$encode["8"] = "1101010101"
$encode["9"] = "110101011"
$encode["0"] = "11 11 11 11 11 11"
$encode[" "] = "2"



$encoder = "snifftech taking over 2022"
$encoded = $null;
$encoder.ToCharArray() | ForEach-Object { 
$str = $_.ToString();
Write-Host $str "=>" $encode[$str]
    $encoded += $encode[$str];
    if($str -notlike " ")
    {
        $encoded += "2";
    }

  }
  Write-Host "ENCODED:" $encoded

## ENCODER - END
 
$code = "1101012121010101121101101210101121011012101011221101011211012101101010121011011210101221101011012110110101012110101012101010110121011012";#$encoded;
$code = $code -replace ("22", "3");
$code = $code -replace ("11", "4");
$split = $code.ToCharArray();
$state = 0;

if([System.Windows.Input.Keyboard]::IsKeyToggled([System.Windows.Input.Key]::CapsLock))
{
    Write-Host "State is on... initiating reset sequence."
    $state = 1;
    $init | ForEach-Object {
        if($_ -eq 0)
        {
            $wsh.SendKeys("{CAPSLOCK}")
        }else
        {
            $wsh.SendKeys("{CAPSLOCK}")
        }
        Start-Sleep -Milliseconds 333
    }
    $state = 0;
    Write-Host "Ready to send message."
}

$split | ForEach-Object {
[int]$i = $_.ToString();
$state = [System.Windows.Input.Keyboard]::IsKeyToggled([System.Windows.Input.Key]::CapsLock);
$p = "";
    
    if(($i -eq 0))
    {
        if($state -eq $true) { $wsh.SendKeys("{CAPSLOCK}") } #turn off
    }elseif(($i -eq 1))
    {
        if($state -eq $false) { $wsh.SendKeys("{CAPSLOCK}") } #turn on
        $p = "."
    }elseif($i -eq 4){
        if($state -eq $false) { $wsh.SendKeys("{CAPSLOCK}") } #turn on
        Start-Sleep -Milliseconds 500
        $p = "-"
    }elseif($i -eq 2)
    {
        if($state -eq $true) { $wsh.SendKeys("{CAPSLOCK}") } #turn off
        Start-Sleep -Milliseconds 500
        $p = " "
    }elseif($i -eq 3)
    {
        if($state -eq $true) { $wsh.SendKeys("{CAPSLOCK}") } #turn off
        Start-Sleep -Milliseconds 500
        $p = " / "
    }else
    {
        Write-Host "error: " + $i 
    }

    Write-Host $p -NoNewline;
    Start-Sleep -Milliseconds 500
}

if([System.Windows.Input.Keyboard]::IsKeyToggled([System.Windows.Input.Key]::CapsLock))
{
    Write-Host "State is on... initiating reset sequence."
    $state = 1;
    $init | ForEach-Object {
        if($_ -eq 0)
        {
            $wsh.SendKeys("{CAPSLOCK}")
        }else
        {
            $wsh.SendKeys("{CAPSLOCK}")
        }
        Start-Sleep -Milliseconds 333
    }
    $state = 0;
    Write-Host "Ready to send message."
}