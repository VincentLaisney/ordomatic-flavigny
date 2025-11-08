<?php
    $PYTHON = 'export PATH="/usr/bin/python3:$PATH"; ';
    shell_exec($PYTHON."python3 ../python/ordomatic_main.py ${_POST["year"]}");
    putenv('TEXMFVAR=' . __DIR__ . '/.texlive2024');
    $retour = shell_exec("/usr/local/bin/lualatex ../latex/${_POST["year"]}.tex; mv ${_POST["year"]}.* ../latex; rm ../latex/*.log; rm ../latex/*.aux");
    print($retour);
?>
