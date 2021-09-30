from SMLImageAnalyzer import SMLImageAnalyzer


analyzer = SMLImageAnalyzer("bird.jpg")
analyzer.remove_background()
analyzer.save_nobackground_image()
analyzer.show_image()
analyzer.show_nobackground_image()
analyzer.wait()
