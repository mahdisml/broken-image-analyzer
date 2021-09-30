import cv2
import copy


class SMLImageAnalyzer:
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path, cv2.IMREAD_COLOR)
        self.gray = cv2.imread(path, 0)
        self.h = len(self.image)
        self.w = len(self.image[0])

        # perceptron

        self.w = []
        self.b = 0.0

        print("SMLImageAnalyzer initialized")

    def improve_contrast(self):
        self.contrast_image = copy.deepcopy(self.image)
        img = self.contrast_image
        a = 1.2
        rg = len(self.contrast_image)
        for i in range(0, rg):
            print(f"{i + 1}/{rg}")
            for j in range(0, len(self.contrast_image[i])):
                img[i][j][0] = self.safe((a * (img[i][j][0] - 128) + 128))
                img[i][j][1] = self.safe((a * (img[i][j][1] - 128) + 128))
                img[i][j][2] = self.safe((a * (img[i][j][2] - 128) + 128))

    def show_image(self):
        cv2.imshow('image', self.image)

    def show_contrast_image(self):
        cv2.imshow('contrast image', self.contrast_image)

    def show_nobackground_image(self):
        cv2.imshow('nobackground image', self.nobackground_image)

    def show_detect_image(self):
        cv2.imshow('detect image', self.detectimage)

    def wait(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_contrast_image(self):
        cv2.imwrite("contrast-" + self.path, self.contrast_image)

    def save_nobackground_image(self):
        cv2.imwrite("nobackground-" + self.path, self.nobackground_image)

    def waiting (self,ii,jj):
        if ("a5" in self.path) and ii == 32 and jj == 32:
            print(f"FOUND IT ! ITS 1")
            self.paint(ii, jj)

        # def wait(self):
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        #
        # def save_contrast_image(self):
        #     cv2.imwrite("contrast-" + self.path, self.contrast_image)
        #
        # def save_nobackground_image(self):
        #     cv2.imwrite("nobackground-" + self.path, self.nobackground_image)
        if ("a3" in self.path) and ii == 10 and jj == 50:
            print(f"FOUND IT ! ITS 1")
            self.paint(ii, jj)
            #     cv2.imwrite("contrast-" + self.path, self.contrast_image)
            #
            # def save_nobackground_image(self):
            #     cv2.imwrite("nobackground-" + self.path, self.nobackground_image)
        if ("c4" in self.path) and ii == 50 and jj == 70:
            print(f"FOUND IT ! ITS 3")
            self.paint(ii, jj)

    def safe(self, num):
        if num > 255:
            return 255
        elif num < 0:
            return 0
        else:
            return num

    def remove_background(self):
        self.nobackground_image = copy.deepcopy(self.image)
        # edges = cv2.Canny(self.image, 100, 200)
        img = self.nobackground_image
        rg = round(len(self.nobackground_image) / 3) * 2
        rg2 = round(len(self.nobackground_image[0]) / 3) * 2
        i = round(len(self.nobackground_image) / 3)
        list = []

        while i + 10 < rg:
            j = round(len(self.nobackground_image[0]) / 3)
            print(f"{i + 1}/{rg}")
            while j + 10 < rg2:
                temp_colors = []
                for ii in range(i, i + 10):
                    for jj in range(j, j + 10):
                        this_color = [
                            self.color(img[ii][jj][0]), self.color(img[ii][jj][1]), self.color(img[ii][jj][2])
                        ]
                        it_was_there = False
                        for m in temp_colors:
                            if m[0] == this_color:
                                m[1] = m[1] + 1
                                it_was_there = True
                            break
                        if not it_was_there:
                            temp_colors.append([this_color, 0])
                temp_colors = sorted(temp_colors, key=lambda color: color[1], reverse=True)
                main_color = temp_colors[0]
                it_was_there = False
                for m in list:
                    if m[0] == main_color:
                        m[1] = m[1] + 1
                        it_was_there = True
                        break
                if not it_was_there:
                    list.append([main_color, 0])
                j = j + 10
            i = i + 10
        list = sorted(list, key=lambda color: color[1], reverse=True)

        # writing
        i = 0
        rg = len(self.nobackground_image)
        rg2 = len(self.nobackground_image[0])
        while i + 10 < rg:
            j = 0
            print(f"{i + 1}/{rg}")
            while j + 10 < rg2:
                temp_colors = []
                for ii in range(i, i + 10):
                    for jj in range(j, j + 10):
                        this_color = [
                            self.color(img[ii][jj][0]), self.color(img[ii][jj][1]), self.color(img[ii][jj][2])
                        ]
                        it_was_there = False
                        for m in temp_colors:
                            if m[0] == this_color:
                                m[1] = m[1] + 1
                                it_was_there = True
                            break
                        if not it_was_there:
                            temp_colors.append([this_color, 0])
                temp_colors = sorted(temp_colors, key=lambda color: color[1], reverse=True)
                main_color = temp_colors[0]
                if main_color == list[0][0]:
                    for ii in range(i, i + 10):
                        for jj in range(j, j + 10):
                            img[ii][jj][0] = 0
                            img[ii][jj][1] = 0
                            img[ii][jj][2] = 0
                j = j + 10
            i = i + 10
        # for i in range(0, rg):
        #     print(f"{i + 1}/{rg}")
        #     for j in range(0, rg2):
        #         img[i][j][0] = img[i][j][0]
        print("end")

    def color(self, color):
        if 127.5 < color <= 255:
            return 1
        else:
            return 0

    def position(self, m, n):
        return 0

    def learn(self, path_list):
        self.data = []
        dim = (50, 50)
        for i in path_list:
            img = cv2.imread(i[0], 0)
            img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            x = []
            for m in img:
                for n in m:
                    x.append(n)
            self.data.append([x, i[1]])
        for i in self.data:
            self.learning(i[0],i[1])
        print("learning done")

    def detect (self):
        self.detectimage = copy.deepcopy(self.gray)
        img = self.detectimage
        rg = len(self.detectimage)
        rg2 = len(self.detectimage[0])
        list = []
        i = 0
        while i + 50 < rg:
            j = 0
            print(f"{i + 1}/{rg}")
            while j + 50 < rg2:
                self.check(i,j)
                j = j + 1
            i = i + 1


    def check (self,ii,jj):
        img = self.detectimage
        rg = ii + 50
        rg2 = jj + 50
        list = []
        i = ii
        while i < rg:
            j = jj
            while j < rg2:
                list.append(img[i][j])
                j = j + 1
            i = i + 1

        comp = self.compute(list)
        if comp != 0:
            print(f"FOUND IT ! ITS {comp}")
            self.paint(ii, jj)
        self.waiting (ii,jj)


    def paint(self,ii,jj):
        img = self.detectimage
        rg = ii + 50
        rg2 = jj + 50
        i = ii
        while i < rg:
            j = jj
            while j < rg2:
                if i == ii or i == ii + 49 or i == ii + 48 or j == jj or j == jj + 49 or j == jj + 48:
                    img[i][j] = 255
                j = j + 1
            i = i + 1

    def learning(self,x,y):
        try:
            m = 0
            changed = False
            l = 0
            while True:
                l = l+ 1
                if m == len(self.w) - 1:
                    m = 0
                if (not changed):
                    break
                if l > 10000 :
                    break
            for i in range (0,y):
                self.w.append(0)
            if self.compute(x) != y:
                try:
                    self.w[i] += self.w * x[i][i].toDouble() * y[i].toDouble()
                except:
                    pass
                self.w[i] += self.w * y[i].toDouble()
                self.w[i] += self.w * x[i][i].toDouble()
                self.w[i] += x[i][i].toDouble() * y[i].toDouble()

                changed = True
        except:
            pass

        return 2
    def compute(self,x):
        yin = 0.0
        i = 0
        while i < len(self.w):
            yin = yin + (self.w[i]* x[i])
            i = i + 1
        yin = yin + self.b

        teta1 = 0.2
        teta2 = 0.3
        teta3 = 0.4
        teta4 = 0.5
        teta5 = 0.6

        if yin <= teta1:
            return 0
        elif teta1 <= yin < teta2:
            return 1
        elif teta2 <= yin < teta3:
            return 2
        elif teta3 <= yin < teta4:
            return 3
        elif teta4 <= yin < teta5:
            return 4
        elif teta5 <= yin:
            return 5
        return 0