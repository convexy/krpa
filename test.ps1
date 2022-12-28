$form = New-Object System.Windows.Forms.Form -Property @{
    Text = "test"
}

$lbl = New-Object System.Windows.Forms.Label -Property @{
    Text = "Name"
    Location = New-Object System.Drawing.Point(10, 10)
    Size = New-Object System.Drawing.Size(50, 20)
}

$tb = New-Object System.Windows.Forms.TextBox -Property @{
    Location = New-Object System.Drawing.Point(60, 10)
    Size = New-Object System.Drawing.Size(70, 20)
}

$tb2 = New-Object System.Windows.Forms.TextBox -Property @{
    Location = New-Object System.Drawing.Point(130, 10)
    Size = New-Object System.Drawing.Size(70, 20)
}


$btn = New-Object System.Windows.Forms.Button -Property @{
    Text = "Exec"
    Location = New-Object System.Drawing.Point(60, 35)
    Size = New-Object System.Drawing.Size(70, 25)
}

$btn2 = New-Object System.Windows.Forms.Button -Property @{
    Text = "Exec2"
    Location = New-Object System.Drawing.Point(60, 65)
    Size = New-Object System.Drawing.Size(70, 25)
}


$form.Controls.Add($lbl)
$form.Controls.Add($tb)
$form.Controls.Add($tb2)
$form.Controls.Add($btn)
$form.Controls.Add($btn2)

$form.ShowDialog()