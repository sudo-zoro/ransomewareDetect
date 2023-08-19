rule ransomware_detected
{
    meta:
        description = "Detects simple Python ransomware"
    strings:
        $python_code = "b64encode(content.encode('utf-8'))"
        $rule2 = "open(filename + \".encrypted\" , 'w')"
        $rule3= "def encrypt_file(self, filename):"
        $rule4= "os.remove(filename)"
    condition:
        $python_code or $rule2 or $rule3 or $rule4
    
}
