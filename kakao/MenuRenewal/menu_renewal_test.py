inputs = [{
        'orders': ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
        'course': [2, 3, 4],
        'result': ["AC", "ACDE", "BCFG", "CDE"]
    }, {
        'orders': ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
        'course': [2, 3, 5],
        'result': ["ACD", "AD", "ADE", "CD", "XYZ"]
    }, {
        'orders': ["XYZ", "XWY", "WXA"],
        'course': [2, 3, 4],
        'result': ["WX", "XY"]
    }]

import menu_renewal
import menu_renewal_counter

for input in inputs:
    if menu_renewal.renew_menu(input['orders'], input['course']) == input['result']:
        print("Passed a test case!")
    else:
        print("Failed a test case!")

for input in inputs:
    if menu_renewal_counter.renew_menu(input['orders'], input['course']) == input['result']:
        print("Passed a test case!")
    else:
        print("Failed a test case!")