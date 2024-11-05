# Audio-Converter

#### Select a source audio file and make a lossless conversion:
     - Open a source audio file
     - Select output format and compression level
     - Export

# Compile .UI
`
cd assets/ui
pyside6-uic main_window.ui | Out-File -FilePath main_window_ui.py -Encoding utf8
`