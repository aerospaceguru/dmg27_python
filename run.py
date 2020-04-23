from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('pavcalculator.html')


@app.route("/calculate", methods=['GET', 'POST'])
def result():
    try:
        if request.form['pavType'] == "Rigid":
            try:
                result = rigid()
            except:
                return "Error. Please check all inputs have been entered."
        else:
            try:
                result = flexible()
            except:
                return "Error. Please check all inputs have been entered."
    except:
        return "Error. Please enter pavement type."

    return render_template('calculation.html', result=result)


def rigid():
    acnR = float(request.form['acnDesign'])
    gearR = request.form['gearDrop']
    coveragesR = request.form['coveragesDrop']
    polyR = 0
    k = int(request.form['kDrop'])
    concrete = request.form['concreteDrop']

    # RIGID CHART DATA

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

    # F5 RIGID EVALUATION
    if concrete == "F5":

        if coveragesR == "Low" and gearR == "Single":
            polyR = f5low[int(int((k - 20) / 10))][0]

        elif coveragesR == "Low" and gearR == "Dual":
            polyR = f5low[int(int((k - 20) / 10))][1]

        elif coveragesR == "Low" and gearR == "Dual-tandem":
            polyR = f5low[int(int((k - 20) / 10))][2]

        elif coveragesR == "Low" and gearR == "Tridem":
            polyR = f5low[int(int((k - 20) / 10))][3]

        elif coveragesR == "Medium" and gearR == "Single":
            polyR = f5med[int(int((k - 20) / 10))][0]

        elif coveragesR == "Medium" and gearR == "Dual":
            polyR = f5med[int(int((k - 20) / 10))][1]

        elif coveragesR == "Medium" and gearR == "Dual-tandem":
            polyR = f5med[int(int((k - 20) / 10))][2]

        elif coveragesR == "Medium" and gearR == "Tridem":
            polyR = f5med[int(int((k - 20) / 10))][3]

    # F6 RIGID EVALUATION
    if concrete == "F6":

        if coveragesR == "Low" and gearR == "Single":
            polyR = f6low[int((k - 20) / 10)][0]

        elif coveragesR == "Low" and gearR == "Dual":
            polyR = f6low[int((k - 20) / 10)][1]

        elif coveragesR == "Low" and gearR == "Dual-tandem":
            polyR = f6low[int((k - 20) / 10)][2]

        elif coveragesR == "Low" and gearR == "Tridem":
            polyR = f6low[int((k - 20) / 10)][3]

        elif coveragesR == "Medium" and gearR == "Single":
            polyR = f6med[int((k - 20) / 10)][0]

        elif coveragesR == "Medium" and gearR == "Dual":
            polyR = f6med[int((k - 20) / 10)][1]

        elif coveragesR == "Medium" and gearR == "Dual-tandem":
            polyR = f6med[int((k - 20) / 10)][2]

        elif coveragesR == "Medium" and gearR == "Tridem":
            polyR = f6med[int((k - 20) / 10)][3]

    answer = polyR
    answer = (np.round(answer / 5.0)) * 5.0
    answer = int(answer)
    gsb = 100

    # LEAN MIX (RIGID) EVALUATION BEGINS

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

    ans = [answer, dlc, gsb, "mm PQC", "mm DLC", "mm GSB"]
    return ans


def flexible():
    acnF = float(request.form['acnDesign'])
    gearF = request.form['gearDrop']
    coveragesF = request.form['coveragesDrop']
    polyF = 0
    cbr = int(request.form['cbrDrop'])
    material = request.form['materialDrop']

    matrix5 = np.array([
        [-0.0128 * np.power(acnF, 2) + 6.4842 * acnF + 127.4725, -0.0127 * np.power(acnF, 2) + 6.5005 * acnF + 145.1648,
         -0.0246 * np.power(acnF, 2) + 8.9962 * acnF + 137.5000,
         - 0.0186 * np.power(acnF, 2) + 8.1131 * acnF + 137.7622],
        [-0.0148 * np.power(acnF, 2) + 6.1930 * acnF + 118.2967, -0.0134 * np.power(acnF, 2) + 6.0868 * acnF + 130.7692,
         -0.0246 * np.power(acnF, 2) + 8.0871 * acnF + 137.5000,
         - 0.0204 * np.power(acnF, 2) + 7.5612 * acnF + 133.5664],
        [-0.0140 * np.power(acnF, 2) + 5.8323 * acnF + 107.6374, -0.0153 * np.power(acnF, 2) + 5.1634 * acnF + 109.6703,
         -0.0313 * np.power(acnF, 2) + 8.4981 * acnF + 107.9167,
         - 0.0205 * np.power(acnF, 2) + 7.2902 * acnF + 120.6294],
        [-0.0129 * np.power(acnF, 2) + 5.4435 * acnF + 114.7253, -0.0129 * np.power(acnF, 2) + 5.6521 * acnF + 111.5385,
         -0.0265 * np.power(acnF, 2) + 7.9167 * acnF + 101.6667,
         - 0.0197 * np.power(acnF, 2) + 6.9930 * acnF + 119.4056],
        [-0.0125 * np.power(acnF, 2) + 5.3610 * acnF + 101.3187, -0.0129 * np.power(acnF, 2) + 5.4435 * acnF + 114.7253,
         -0.0246 * np.power(acnF, 2) + 7.4811 * acnF + 110.8333,
         - 0.0174 * np.power(acnF, 2) + 6.5097 * acnF + 119.0559],
        [-0.0111 * np.power(acnF, 2) + 5.0869 * acnF + 104.7253, -0.0115 * np.power(acnF, 2) + 5.2465 * acnF + 103.4615,
         -0.0180 * np.power(acnF, 2) + 6.6610 * acnF + 115.4167,
         - 0.0194 * np.power(acnF, 2) + 6.8444 * acnF + 98.6014],
        [-0.0105 * np.power(acnF, 2) + 4.7464 * acnF + 113.9560, -0.0111 * np.power(acnF, 2) + 5.0869 * acnF + 104.7253,
         -0.0284 * np.power(acnF, 2) + 7.6553 * acnF + 90.8333,
         - 0.0190 * np.power(acnF, 2) + 6.6134 * acnF + 102.7972],
        [-0.0105 * np.power(acnF, 2) + 4.8535 * acnF + 100.3846, -0.0101 * np.power(acnF, 2) + 4.9573 * acnF + 107.0879,
         -0.0256 * np.power(acnF, 2) + 7.3580 * acnF + 88.7500,
         - 0.0150 * np.power(acnF, 2) + 6.1364 * acnF + 101.3986],
        [-0.011675824 * np.power(acnF, 2) + 5.028846154 * acnF + 90.87912088,
         -0.009473982 * np.power(acnF, 2) + 4.631908533 * acnF + 111.0989011,
         -0.0199 * np.power(acnF, 2) + 6.7633 * acnF + 89.5833,
         -0.017732268 * np.power(acnF, 2) + 6.301198801 * acnF + 99.47552448],
        [-0.008686167 * np.power(acnF, 2) + 4.389786684 * acnF + 103.956044,
         -0.009837589 * np.power(acnF, 2) + 4.797228507 * acnF + 95.87912088,
         -0.0227 * np.power(acnF, 2) + 6.8939 * acnF + 88.3333,
         -0.01486014 * np.power(acnF, 2) + 5.885364635 * acnF + 106.6433566],
        [-0.00779735 * np.power(acnF, 2) + 4.265433096 * acnF + 104.8901099,
         -0.010322398 * np.power(acnF, 2) + 4.731940853 * acnF + 95.10989011,
         -0.0180 * np.power(acnF, 2) + 6.2822 * acnF + 98.7500,
         -0.016983017 * np.power(acnF, 2) + 6.031468531 * acnF + 96.32867133],
        [-0.009837589 * np.power(acnF, 2) + 4.475799935 * acnF + 96.59340659,
         -0.008686167 * np.power(acnF, 2) + 4.389786684 * acnF + 103.956044,
         -0.023674242 * np.power(acnF, 2) + 6.785984848 * acnF + 82.91666667,
         -0.014985015 * np.power(acnF, 2) + 5.834165834 * acnF + 91.78321678],
        [-0.005999515 * np.power(acnF, 2) + 3.772422431 * acnF + 112.8021978,
         -0.009473982 * np.power(acnF, 2) + 4.506908533 * acnF + 96.0989011,
         -0.017045455 * np.power(acnF, 2) + 6.132575758 * acnF + 85.83333333,
         -0.011738262 * np.power(acnF, 2) + 5.26973027 * acnF + 103.1468531]
    ])

    matrix7 = np.array([
        [-0.019089367 * np.power(acnF, 2) + 8.438227214 * acnF + 182.7472527,
         -0.018261151 * np.power(acnF, 2) + 8.49321267 * acnF + 189.8351648,
         -0.036931818 * np.power(acnF, 2) + 11.7594697 * acnF + 185.4166667,
         -0.026973027 * np.power(acnF, 2) + 10.50699301 * acnF + 192.1328671],
        [-0.015534098 * np.power(acnF, 2) + 7.405098578 * acnF + 159.3406593,
         -0.018988365 * np.power(acnF, 2) + 8.055995475 * acnF + 155.8241758,
         -0.028409091 * np.power(acnF, 2) + 10.15530303 * acnF + 165.8333333,
         -0.026973027 * np.power(acnF, 2) + 10.50699301 * acnF + 192.1328671],
        [-0.016968326 * np.power(acnF, 2) + 7.214932127 * acnF + 143.0769231,
         -0.017877343 * np.power(acnF, 2) + 7.547874919 * acnF + 138.956044,
         -0.03125 * np.power(acnF, 2) + 9.785984848 * acnF + 149.5833333,
         -0.02047952 * np.power(acnF, 2) + 8.553946054 * acnF + 157.1678322],
        [-0.016604719 * np.power(acnF, 2) + 7.03175501 * acnF + 114.7252747,
         -0.017493536 * np.power(acnF, 2) + 7.191822883 * acnF + 130.9340659,
         -0.03219697 * np.power(acnF, 2) + 9.678030303 * acnF + 124.1666667,
         -0.022977023 * np.power(acnF, 2) + 8.546453546 * acnF + 138.8111888],
        [-0.014766484 * np.power(acnF, 2) + 6.514423077 * acnF + 117.5824176,
         -0.015251293 * np.power(acnF, 2) + 6.699135423 * acnF + 116.8131868,
         -0.015251293 * np.power(acnF, 2) + 6.699135423 * acnF + 116.8131868,
         -0.020104895 * np.power(acnF, 2) + 7.828421578 * acnF + 142.1328671],
        [-0.013675663 * np.power(acnF, 2) + 6.17917744 * acnF + 110.3846154,
         -0.015433096 * np.power(acnF, 2) + 6.505009696 * acnF + 113.8461538,
         -0.024621212 * np.power(acnF, 2) + 8.359848485 * acnF + 122.5,
         -0.020104895 * np.power(acnF, 2) + 7.828421578 * acnF + 117.1328671],
        [-0.012342437 * np.power(acnF, 2) + 5.769432773 * acnF + 117.1428571,
         -0.013796865 * np.power(acnF, 2) + 6.162855527 * acnF + 107.6923077,
         -0.022727273 * np.power(acnF, 2) + 8.03030303 * acnF + 113.3333333,
         -0.019230769 * np.power(acnF, 2) + 7.445054945 * acnF + 125],
        [-0.010746606 * np.power(acnF, 2) + 5.469457014 * acnF + 114.6153846,
         -0.012726244 * np.power(acnF, 2) + 5.875484809 * acnF + 110.1648352,
         -0.026515152 * np.power(acnF, 2) + 8.189393939 * acnF + 111.6666667,
         -0.019230769 * np.power(acnF, 2) + 7.445054945 * acnF + 100],
        [-0.012039431 * np.power(acnF, 2) + 5.551308985 * acnF + 107.0879121,
         -0.010746606 * np.power(acnF, 2) + 5.469457014 * acnF + 114.6153846,
         -0.018939394 * np.power(acnF, 2) + 7.325757576 * acnF + 110,
         -0.021103896 * np.power(acnF, 2) + 7.501248751 * acnF + 100.1748252],
        [-0.011797027 * np.power(acnF, 2) + 5.369667098 * acnF + 104.6153846,
         -0.012039431 * np.power(acnF, 2) + 5.551308985 * acnF + 107.0879121,
         -0.03125 * np.power(acnF, 2) + 8.498106061 * acnF + 82.91666667,
         -0.017107892 * np.power(acnF, 2) + 6.886863137 * acnF + 104.5454545],
        [-0.009150776 * np.power(acnF, 2) + 4.973052683 * acnF + 107.8021978,
         -0.012180834 * np.power(acnF, 2) + 5.475719134 * acnF + 97.63736264,
         -0.025568182 * np.power(acnF, 2) + 7.78219697 * acnF + 90.41666667,
         -0.017232767 * np.power(acnF, 2) + 6.753246753 * acnF + 105.0699301],
        [-0.010544602 * np.power(acnF, 2) + 4.972850679 * acnF + 109.3406593,
         -0.011110213 * np.power(acnF, 2) + 5.295491273 * acnF + 101.5384615,
         -0.026515152 * np.power(acnF, 2) + 7.689393939 * acnF + 91.66666667,
         -0.018106893 * np.power(acnF, 2) + 6.779470529 * acnF + 97.2027972],
        [-0.009776988 * np.power(acnF, 2) + 4.957175178 * acnF + 97.58241758,
         -0.011675824 * np.power(acnF, 2) + 5.153846154 * acnF + 105.8791209,
         -0.024621212 * np.power(acnF, 2) + 7.481060606 * acnF + 85.83333333,
         -0.01510989 * np.power(acnF, 2) + 6.332417582 * acnF + 100]
    ])

    if material == "HSBBM":

        if coveragesF == "Low" and (gearF == "Single" or gearF == "Dual" or gearF == "Dual-tandem"):
            polyF = matrix5[cbr - 3][0]

        elif coveragesF == "Low" and gearF == "Tridem":
            polyF = matrix5[cbr - 3][1]

        elif coveragesF == "Medium" and (gearF == "Single" or gearF == "Dual"):
            polyF = matrix5[cbr - 3][2]

        elif coveragesF == "Medium" and (gearF == "Dual-tandem" or gearF == "Tridem"):
            polyF = matrix5[cbr - 3][3]

        else:
            polyF = 888

    elif material == "BBM":

        if coveragesF == "Low" and (gearF == "Single" or gearF == "Dual" or gearF == "Dual-tandem"):
            polyF = matrix7[cbr - 3][0]

        elif coveragesF == "Low" and gearF == "Tridem":
            polyF = matrix7[cbr - 3][1]

        elif coveragesF == "Medium" and (gearF == "Single" or gearF == "Dual"):
            polyF = matrix7[cbr - 3][2]

        elif coveragesF == "Medium" and (gearF == "Dual-tandem" or gearF == "Tridem"):
            polyF = matrix7[cbr - 3][3]

        else:
            polyF = 888

    answer = polyF
    answer = (np.round(answer / 25.0)) * 25.0
    answer = int(answer)
    gsb = 100
    surface = 100

    ans = [surface, answer, gsb, "mm surfacing", "mm bound base", "mm GSB"]
    return ans


if __name__ == "__main__":
    app.run(debug=True)
