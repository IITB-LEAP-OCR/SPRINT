from teds import get_s_teds

y_true_html = """<html><table>
                <tbody>
                    <tr>
                        <td></td>
                        <td colspan="4"> Amount & Nature of Beneficial Ownership</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td>PCT of</td>
                        <td> Common</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Name of Beneficial</td>
                        <td> Common</td>
                        <td> Common</td>
                        <td> Stock</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Owner and Position</td>
                        <td> Stock</td>
                        <td> Stock</td>
                        <td> Equivalents</td>
                        <td>Total</td>
                    </tr>
                    <tr>
                        <td>Frank M. Clark</td>
                        <td> 1,000(1)</td>
                        <td> *</td>
                        <td> 17,836(14)</td>
                        <td>18,836</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Betsy Z. Cohen</td>
                        <td> 71,484(2)</td>
                        <td> *</td>
                        <td> 69,899(14)</td>
                        <td>141,383</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Molly J. Coye, M.D.</td>
                        <td> 3,642</td>
                        <td> *</td>
                        <td> 19,572(14)</td>
                        <td>23,214</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Roger N. Farah</td>
                        <td> 3,000</td>
                        <td> *</td>
                        <td> 19,855(14)</td>
                        <td>22,855</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Barbara Hackman Franklin</td>
                        <td> 21,623</td>
                        <td> *</td>
                        <td> 45,691(14)</td>
                        <td>67,314</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Jeffrey E. Garten</td>
                        <td> 8,148(3)</td>
                        <td> *</td>
                        <td> 30,731(14)</td>
                        <td>38,879</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Earl G. Graves</td>
                        <td> 57,200(2)</td>
                        <td> *</td>
                        <td> 69,919(14)</td>
                        <td>127,119</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Gerald Greenwald</td>
                        <td> 8,848(4)</td>
                        <td> *</td>
                        <td> 60,351(14)</td>
                        <td>69,199</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Ellen M. Hancock</td>
                        <td> 35,170(5)</td>
                        <td> *</td>
                        <td> 109,110(14)</td>
                        <td>144,280</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Richard J. Harrington</td>
                        <td> 414</td>
                        <td> *</td>
                        <td> 14,962(14)</td>
                        <td>15,376</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Edward J. Ludwig</td>
                        <td> 23,391(6)</td>
                        <td> *</td>
                        <td> 34,645(14)</td>
                        <td>58,036</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Joseph P. Newhouse</td>
                        <td> 37,068(7)</td>
                        <td> *</td>
                        <td> 48,573(14)</td>
                        <td>85,641</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Ronald A. Williams</td>
                        <td> 7,473,850(8)</td>
                        <td> 1.70%</td>
                        <td> 1,182,296(15)</td>
                        <td>8,656,146</td>
                    </tr>
                    <tr>
                        <td>(Chairman, Chief Executive Officer, current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Mark T. Bertolini</td>
                        <td> 1,324,975(9)</td>
                        <td> *</td>
                        <td> 392,918(16)</td>
                        <td>1,717,893</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>William J. Casazza</td>
                        <td> 407,712(10)</td>
                        <td> *</td>
                        <td> 111,035(17)</td>
                        <td>518,747</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Lonny Reisman, M.D.</td>
                        <td> 234,113(11)</td>
                        <td> *</td>
                        <td> 63,542(18)</td>
                        <td>297,655</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Joseph M. Zubretsky</td>
                        <td> 524,572(12)</td>
                        <td> *</td>
                        <td> 271,471(19)</td>
                        <td>796,043</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Directors and executive officers as a group (18 persons)</td>
                        <td> 10,439,474(13)</td>
                        <td> 2.37%</td>
                        <td> 2,687,043(20)</td>
                        <td>13,126,517</td>
                    </tr>
                </tbody>
            </table>
        </html>"""


y_pred_html = """<html><table>
                <tbody>
                    <tr>
                        <td></td>
                        <td colspan="4"> Amount & Nature of Beneficial Ownership</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td>PCT of</td>
                        <td> Common</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Name of Beneficial</td>
                        <td> Common</td>
                        <td> Common</td>
                        <td> Stock</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Owner and Position</td>
                        <td> Stock</td>
                        <td> Stock</td>
                        <td> Equivalents</td>
                        <td>Total</td>
                    </tr>
                    <tr>
                        <td>Frank M. Clark</td>
                        <td> 1,000(1)</td>
                        <td> *</td>
                        <td> 17,836(14)</td>
                        <td>18,836</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Betsy Z. Cohen</td>
                        <td> 71,484(2)</td>
                        <td> *</td>
                        <td> 69,899(14)</td>
                        <td>141,383</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Molly J. Coye, M.D.</td>
                        <td> 3,642</td>
                        <td> *</td>
                        <td> 19,572(14)</td>
                        <td>23,214</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Roger N. Farah</td>
                        <td> 3,000</td>
                        <td> *</td>
                        <td> 19,855(14)</td>
                        <td>22,855</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Barbara Hackman Franklin</td>
                        <td> 21,623</td>
                        <td> *</td>
                        <td> 45,691(14)</td>
                        <td>67,314</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Jeffrey E. Garten</td>
                        <td> 8,148(3)</td>
                        <td> *</td>
                        <td> 30,731(14)</td>
                        <td>38,879</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Earl G. Graves</td>
                        <td> 57,200(2)</td>
                        <td> *</td>
                        <td> 69,919(14)</td>
                        <td>127,119</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Gerald Greenwald</td>
                        <td> 8,848(4)</td>
                        <td> *</td>
                        <td> 60,351(14)</td>
                        <td>69,199</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Ellen M. Hancock</td>
                        <td> 35,170(5)</td>
                        <td> *</td>
                        <td> 109,110(14)</td>
                        <td>144,280</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Richard J. Harrington</td>
                        <td> 414</td>
                        <td> *</td>
                        <td> 14,962(14)</td>
                        <td>15,376</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Edward J. Ludwig</td>
                        <td> 23,391(6)</td>
                        <td> *</td>
                        <td> 34,645(14)</td>
                        <td>58,036</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Joseph P. Newhouse</td>
                        <td> 37,068(7)</td>
                        <td> *</td>
                        <td> 48,573(14)</td>
                        <td>85,641</td>
                    </tr>
                    <tr>
                        <td>(current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Ronald A. Williams</td>
                        <td> 7,473,850(8)</td>
                        <td> 1.70%</td>
                        <td> 1,182,296(15)</td>
                        <td>8,656,146</td>
                    </tr>
                    <tr>
                        <td>(Chairman, Chief Executive Officer, current Director and Nominee)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Mark T. Bertolini</td>
                        <td> 1,324,975(9)</td>
                        <td> *</td>
                        <td> 392,918(16)</td>
                        <td>1,717,893</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>William J. Casazza</td>
                        <td> 407,712(10)</td>
                        <td> *</td>
                        <td> 111,035(17)</td>
                        <td>518,747</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Lonny Reisman, M.D.</td>
                        <td> 234,113(11)</td>
                        <td> *</td>
                        <td> 63,542(18)</td>
                        <td>297,655</td>
                    </tr>
                    <tr>
                        <td>(named )</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Joseph M. Zubretsky</td>
                        <td> 524,572(12)</td>
                        <td> *</td>
                        <td> 271,471(19)</td>
                        <td>796,043</td>
                    </tr>
                    <tr>
                        <td>(named executive)</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Directors and executive officers as a group (18 persons)</td>
                        <td> 10,439,474(13)</td>
                        <td> 2.37%</td>
                        <td> 2,687,043(20)</td>
                        <td>13,126,517</td>
                    </tr>
                </tbody>
            </table>
        </html>"""



score = get_s_teds(y_pred_html, y_true_html)
print(score)