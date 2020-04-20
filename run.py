from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/calculate", methods=['GET', 'POST'])
def result():
    result = calculate()
    return render_template('calculation.html', result=result)


def calculate():
    pavType = request.form['pavType']
    acnR = float(request.form['acnDesign'])
    gearR = request.form['gearDrop']
    coveragesR = request.form['coveragesDrop']
    polyR = 0
    k = int(request.form['kDrop'])
    concrete = request.form['concreteDrop']

    f5low = np.array([
        [-0.017857143 * np.power(acnR, 2) + 4.221428571 * acnR + 121.0,
         -0.012797619 * np.power(acnR, 2) + 3.782738095 * acnR + 124.6428571,
         -0.009440559 * np.power(acnR, 2) + 3.351398601 * acnR + 123.2954545,
         -0.008591409 * np.power(acnR, 2) + 3.171078921 * acnR + 122.5000000],
        [-0.017857143 * np.power(acnR, 2) + 4.157142857 * acnR + 119.5,
         -0.015476190 * np.power(acnR, 2) + 3.934523810 * acnR + 118.9285714,
         -0.009453047 * np.power(acnR, 2) + 3.421203796 * acnR + 117.1590909,
         -0.008429071 * np.power(acnR, 2) + 3.198926074 * acnR + 117.7272727],
        [-0.015178571 * np.power(acnR, 2) + 3.912500000 * acnR + 119.0,
         -0.015476190 * np.power(acnR, 2) + 3.863095238 * acnR + 118.9285714,
         -0.009502997 * np.power(acnR, 2) + 3.488886114 * acnR + 112.6136364,
         -0.007923327 * np.power(acnR, 2) + 3.203983516 * acnR + 114.0340909],
        [-0.016964286 * np.power(acnR, 2) + 3.980357143 * acnR + 116.0,
         -0.013392857 * np.power(acnR, 2) + 3.687500000 * acnR + 118.5714286,
         -0.009902597 * np.power(acnR, 2) + 3.600274725 * acnR + 107.9545455,
         -0.007817183 * np.power(acnR, 2) + 3.247002997 * acnR + 110.4545455],
        [-0.015178571 * np.power(acnR, 2) + 3.798214286 * acnR + 118.0,
         -0.014285714 * np.power(acnR, 2) + 3.767857143 * acnR + 115.7142857,
         -0.009833916 * np.power(acnR, 2) + 3.623688811 * acnR + 107.1022727,
         -0.008035714 * np.power(acnR, 2) + 3.306006494 * acnR + 109.2613636],
        [-0.015178571 * np.power(acnR, 2) + 3.798214286 * acnR + 115.5,
         -0.014285714 * np.power(acnR, 2) + 3.767857143 * acnR + 115.0000000,
         -0.010439560 * np.power(acnR, 2) + 3.736513487 * acnR + 105.3409091,
         -0.008054446 * np.power(acnR, 2) + 3.349525475 * acnR + 108.4090909],
        [-0.015178571 * np.power(acnR, 2) + 3.798214286 * acnR + 115.5,
         -0.013392857 * np.power(acnR, 2) + 3.705357143 * acnR + 117.5000000,
         -0.010089910 * np.power(acnR, 2) + 3.722527473 * acnR + 107.2727273,
         -0.008216783 * np.power(acnR, 2) + 3.377622378 * acnR + 109.5454545]
    ])

    f5med = np.array([
        [-0.019642857 * np.power(acnR, 2) + 4.717857143 * acnR + 125.5,
         -0.015476190 * np.power(acnR, 2) + 4.363095238 * acnR + 126.7857143,
         -0.010083666 * np.power(acnR, 2) + 3.675387113 * acnR + 129.2613636,
         -0.009459291 * np.power(acnR, 2) + 3.519043457 * acnR + 129.3750000],
        [-0.021875000 * np.power(acnR, 2) + 4.774107143 * acnR + 122.75,
         -0.014583333 * np.power(acnR, 2) + 4.211309524 * acnR + 125.3571429,
         -0.010683067 * np.power(acnR, 2) + 3.798763736 * acnR + 123.2386364,
         -0.009496753 * np.power(acnR, 2) + 3.558878621 * acnR + 125.7386364],
        [-0.019642857 * np.power(acnR, 2) + 4.582142857 * acnR + 121.5,
         -0.013095238 * np.power(acnR, 2) + 4.065476190 * acnR + 123.5714286,
         -0.011195055 * np.power(acnR, 2) + 3.924762737 * acnR + 118.2386364,
         -0.010277223 * np.power(acnR, 2) + 3.732892108 * acnR + 118.8636364],
        [-0.021428571 * np.power(acnR, 2) + 4.650000000 * acnR + 118.5,
         -0.014583333 * np.power(acnR, 2) + 4.139880952 * acnR + 120.3571429,
         -0.011700799 * np.power(acnR, 2) + 4.045579421 * acnR + 113.7500000,
         -0.010439560 * np.power(acnR, 2) + 3.799450549 * acnR + 116.2500000],
        [-0.019642857 * np.power(acnR, 2) + 4.517857143 * acnR + 117.5,
         -0.013095238 * np.power(acnR, 2) + 3.994047619 * acnR + 121.0714286,
         -0.011781968 * np.power(acnR, 2) + 4.104208292 * acnR + 112.6704545,
         -0.010339660 * np.power(acnR, 2) + 3.831918082 * acnR + 115.6818182],
        [-0.017410714 * np.power(acnR, 2) + 4.325892857 * acnR + 118.75,
         -0.014583333 * np.power(acnR, 2) + 4.068452381 * acnR + 120.3571429,
         -0.011825674 * np.power(acnR, 2) + 4.154470529 * acnR + 111.9318182,
         -0.010452048 * np.power(acnR, 2) + 3.897227772 * acnR + 114.5454545],
        [-0.017410714 * np.power(acnR, 2) + 4.325892857 * acnR + 118.75,
         -0.014583333 * np.power(acnR, 2) + 4.068452381 * acnR + 122.8571429,
         -0.011725774 * np.power(acnR, 2) + 4.162462537 * acnR + 114.2045455,
         -0.010295954 * np.power(acnR, 2) + 3.904033467 * acnR + 115.9659091],
    ])

    f6low = np.array([
        [-0.013392857 * np.power(acnR, 2) + 3.537500000 * acnR + 104.00,
         -0.011607143 * np.power(acnR, 2) + 3.455357143 * acnR + 107.1428571,
         -0.008610140 * np.power(acnR, 2) + 3.013548951 * acnR + 112.2159091,
         -0.007636114 * np.power(acnR, 2) + 2.8921703300 * acnR + 104.8295455],
        [-0.015625000 * np.power(acnR, 2) + 3.658035714 * acnR + 100.25,
         -0.012500000 * np.power(acnR, 2) + 3.446428571 * acnR + 105.0000000,
         -0.007423826 * np.power(acnR, 2) + 2.908279221 * acnR + 109.7159091,
         -0.006630869 * np.power(acnR, 2) + 2.7990759240 * acnR + 102.7272727],
        [-0.013839286 * np.power(acnR, 2) + 3.475892857 * acnR + 99.75,
         -0.011904762 * np.power(acnR, 2) + 3.345238095 * acnR + 103.9285714,
         -0.006499750 * np.power(acnR, 2) + 2.835352148 * acnR + 109.0340909,
         -0.005407093 * np.power(acnR, 2) + 2.6784465530 * acnR + 103.5227273],
        [-0.016071429 * np.power(acnR, 2) + 3.596428571 * acnR + 96.00,
         -0.010416667 * np.power(acnR, 2) + 3.181547619 * acnR + 105.7142857,
         -0.006106394 * np.power(acnR, 2) + 2.837537463 * acnR + 106.1363636,
         -0.004408092 * np.power(acnR, 2) + 2.5800449550 * acnR + 104.0909091],
        [-0.014285714 * np.power(acnR, 2) + 3.414285714 * acnR + 98.00,
         -0.010416667 * np.power(acnR, 2) + 3.181547619 * acnR + 103.2142857,
         -0.006000250 * np.power(acnR, 2) + 2.850836663 * acnR + 105.7386364,
         -0.003902348 * np.power(acnR, 2) + 2.5378996000 * acnR + 104.7159091],
        [-0.016071429 * np.power(acnR, 2) + 3.532142857 * acnR + 94.50,
         -0.010416667 * np.power(acnR, 2) + 3.181547619 * acnR + 103.2142857,
         -0.005282218 * np.power(acnR, 2) + 2.805569431 * acnR + 106.2500000,
         -0.003558941 * np.power(acnR, 2) + 2.5343406590 * acnR + 104.5454545],
        [-0.016071429 * np.power(acnR, 2) + 3.532142857 * acnR + 94.50,
         -0.009523810 * np.power(acnR, 2) + 3.119047619 * acnR + 106.0714286,
         -0.005126124 * np.power(acnR, 2) + 2.812375125 * acnR + 107.6704545,
         -0.003902348 * np.power(acnR, 2) + 2.6043331670 * acnR + 104.1477273],
    ])

    f6med = np.array([
        [-0.020089286 * np.power(acnR, 2) + 4.091964286 * acnR + 112.25,
         -0.010416667 * np.power(acnR, 2) + 3.395833333 * acnR + 119.6428571,
         -0.008877373 * np.power(acnR, 2) + 3.126960539 * acnR + 117.6250000,
         -0.008098152 * np.power(acnR, 2) + 2.983703796 * acnR + 113.4659091],
        [-0.021875000 * np.power(acnR, 2) + 4.159821429 * acnR + 109.25,
         -0.010416667 * np.power(acnR, 2) + 3.324404762 * acnR + 117.8571429,
         -0.008229271 * np.power(acnR, 2) + 3.092532468 * acnR + 113.9772727,
         -0.006699550 * np.power(acnR, 2) + 2.826361139 * acnR + 114.0340909],
        [-0.019642857 * np.power(acnR, 2) + 3.967857143 * acnR + 108.00,
         -0.010119048 * np.power(acnR, 2) + 3.255952381 * acnR + 116.0714286,
         -0.007086663 * np.power(acnR, 2) + 2.995566933 * acnR + 113.4659091,
         -0.005294705 * np.power(acnR, 2) + 2.693556444 * acnR + 114.4318182],
        [-0.021875000 * np.power(acnR, 2) + 4.088392857 * acnR + 104.25,
         -0.008630952 * np.power(acnR, 2) + 3.110119048 * acnR + 116.7857143,
         -0.006637113 * np.power(acnR, 2) + 2.984328172 * acnR + 111.7613636,
         -0.004795205 * np.power(acnR, 2) + 2.677572428 * acnR + 111.9318182],
        [-0.019642857 * np.power(acnR, 2) + 3.853571429 * acnR + 107.00,
         -0.008630952 * np.power(acnR, 2) + 3.092261905 * acnR + 115.3571429,
         -0.006824426 * np.power(acnR, 2) + 3.057629870 * acnR + 109.2613636,
         -0.004395604 * np.power(acnR, 2) + 2.653596404 * acnR + 112.1590909],
        [-0.019642857 * np.power(acnR, 2) + 3.853571429 * acnR + 104.50,
         -0.008630952 * np.power(acnR, 2) + 3.110119048 * acnR + 114.2857143,
         -0.006880619 * np.power(acnR, 2) + 3.081543457 * acnR + 109.8863636,
         -0.003896104 * np.power(acnR, 2) + 2.637612388 * acnR + 112.1590909],
        [-0.019642857 * np.power(acnR, 2) + 3.853571429 * acnR + 104.50,
         -0.010119048 * np.power(acnR, 2) + 3.273809524 * acnR + 112.5000000,
         -0.007067932 * np.power(acnR, 2) + 3.123376623 * acnR + 110.6818182,
         -0.004395604 * np.power(acnR, 2) + 2.720029970 * acnR + 111.5909091],
    ])

    if concrete == "F5":

        if coveragesR == "Low" and gearR == "Single":
            polyR = f5low[int((k - 20) / 10)][0]

        elif coveragesR == "Low" and gearR == "Dual":
            polyR = f5low[int((k - 20) / 10)][1]
            print(polyR)

        elif coveragesR == "Low" and gearR == "Dual-tandem":
            polyR = f5low[int((k - 20) / 10)][2]

        elif coveragesR == "Low" and gearR == "Tridem":
            polyR = f5low[int((k - 20) / 10)][3]

        elif coveragesR == "Medium" and gearR == "Single":
            polyR = f5med[int((k - 20) / 10)][0]

        elif coveragesR == "Medium" and gearR == "Dual":
            polyR = f5med[int((k - 20) / 10)][1]

        elif coveragesR == "Medium" and gearR == "Dual-tandem":
            polyR = f5med[int((k - 20) / 10)][2]

        elif coveragesR == "Medium" and gearR == "Tridem":
            polyR = f5med[int((k - 20) / 10)][3]

        answer = polyR
        answer = (np.round(answer / 5.0)) * 5.0
        answer = int(answer)
        gsbrigidsoln = 100

        dlc = ''

        boundarySing59 = 1.858974359 * k + 147.8205128
        boundarySing79 = 1.779661017 * k + 84.40677966
        boundaryDual59 = 1.602564103 * k + 160.4487179
        boundaryDual79 = 1.602564103 * k + 95.44871795
        boundaryDtan39 = 2.105263158 * k + 257.8947368
        boundaryDtan56 = 2.083333333 * k + 198.3333333
        boundaryDtan69 = 2.193877551 * k + 131.122449
        boundaryDtan79 = 2.033898305 * k + 79.3220339

        if gearR == "Single":

            if k < 60:
                if answer >= boundarySing59:
                    dlc = "150"
                elif (answer < boundarySing59) and (answer >= boundarySing79):
                    dlc = "125"
                else:
                    dlc = "100"

            elif 60 <= k <= 79:
                if answer >= boundarySing79:
                    dlc = "125"
                else:
                    dlc = "100"

            else:
                dlc = "100"

        elif gearR == "Dual":

            if k < 60:
                if answer >= boundaryDual59:
                    dlc = "150"
                elif (answer < boundaryDual59) and (answer >= boundaryDual79):
                    dlc = "125"
                else:
                    dlc = "100"

            elif 60 <= k <= 79:
                if answer >= boundaryDual79:
                    dlc = "125"
                else:
                    dlc = "100"

            else:
                dlc = "100"

        elif gearR == "Dual-tandem" or gearR == "Tridem":

            if k < 40:
                if answer >= boundaryDtan39:
                    dlc = "200"
                elif (answer < boundaryDtan39) and (answer >= boundaryDtan56):
                    dlc = "175"
                elif (answer < boundaryDtan56) and (answer >= boundaryDtan69):
                    dlc = "150"
                elif (answer < boundaryDtan69) and (answer >= boundaryDtan79):
                    dlc = "125"
                else:
                    dlc = "100"

            elif 40 <= k <= 56:
                if answer >= boundaryDtan56:
                    dlc = "175"
                elif (answer < boundaryDtan56) and (answer >= boundaryDtan69):
                    dlc = "150"
                elif (answer < boundaryDtan69) and (answer >= boundaryDtan79):
                    dlc = "125"
                else:
                    dlc = "100"

            elif 56 <= k <= 69:
                if answer >= boundaryDtan69:
                    dlc = "150"
                elif (answer < boundaryDtan69) and (answer >= boundaryDtan79):
                    dlc = "125"
                else:
                    dlc = "100"

            elif 69 <= k <= 79:
                if answer >= boundaryDtan79:
                    dlc = "125"

            else:
                dlc = "100"

        else:
            dlc = "100"

        ans = [answer, dlc, gsbrigidsoln]
        return ans


if __name__ == "__main__":
    app.run(debug=True)
