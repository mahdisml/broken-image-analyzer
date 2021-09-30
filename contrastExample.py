from SMLImageAnalyzer import SMLImageAnalyzer


analyzer = SMLImageAnalyzer("winter.jpg")
analyzer.improve_contrast()
analyzer.save_contrast_image()
analyzer.show_image()
analyzer.show_contrast_image()
analyzer.wait()
