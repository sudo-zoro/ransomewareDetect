rule ransomware_key
{
    meta:
        description = "Detects ransomware key"
        author = "Your Name"
        reference = "None"
    strings:
        $key = "rankey"
        $encryption = "b64encode(content.encode('utf-8'))"
    condition:
        $key or $encryption
}
