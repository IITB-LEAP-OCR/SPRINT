from utility.teds.metric import TEDS

def clean_html(html_):
    def replace_html_attr(html_):
        tag_list = ["<thead>", "</thead>", "<tbody>", "</tbody>", "<sup>", "</sup>", "<sub>", "</sub>", "\xa0", "<p>", "</p>",
                    'colspan="0"', 'colspan="1"', 'colspan="2"', 'colspan="3"', 'colspan="4"',
                    'colspan="5"', 'colspan="6"', 'colspan="7"', 'colspan="8"', 'colspan="9"',
                    'colspan="10"', 'colspan="11"', 'colspan="12"', 'colspan="13"', 'colspan="14"', 
                    'colspan="15"', 'colspan="16"', 'colspan="17"', 'colspan="18"', 'colspan="19"', 
                    'colspan="20"', 'colspan="21"', 'colspan="22"', 'colspan="23"', 'colspan="24"', 
                    'colspan="25"', 'colspan="26"', 'colspan="27"', 'colspan="28"', 'colspan="29"', 'colspan="30"',
                    'rowspan="0"', 'rowspan="1"', 'rowspan="2"', 'rowspan="3"', 'rowspan="4"', 
                    'rowspan="5"', 'rowspan="6"', 'rowspan="7"', 'rowspan="8"', 'rowspan="9"',
                    'rowspan="10"', 'rowspan="11"', 'rowspan="12"', 'rowspan="13"', 'rowspan="14"', 
                    'rowspan="15"', 'rowspan="16"', 'rowspan="17"', 'rowspan="18"', 'rowspan="19"', 
                    'rowspan="20"', 'rowspan="21"', 'rowspan="22"', 'rowspan="23"', 'rowspan="24"', 
                    'rowspan="25"', 'rowspan="26"', 'rowspan="27"', 'rowspan="28"', 'rowspan="29"', 'rowspan="30"']
        for tag in tag_list:
            html_ = html_.replace(tag, "")
        html_ = html_.replace("<th","<td")
        html_ = html_.replace("</th>","</td>")
        return html_
    html_ = ' '.join(html_.split())
    return replace_html_attr(html_)

def get_s_teds(pred_html, true_html):
    teds = TEDS()
    final_pred_html = clean_html(pred_html)
    final_true_html = clean_html(true_html)
    # print(final_pred_html)
    # print(final_true_html)
    # print()
    score = teds.evaluate(final_pred_html, final_true_html, True)
    return score

# print(f"The ted score of html structure : {teds.evaluate(y_pred_html,y_true_html, True)}")
# print(f"The ted score of html table     : {teds.evaluate(y_true_html,y_pred_html)}")
