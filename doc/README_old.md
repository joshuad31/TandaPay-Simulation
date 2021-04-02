# TandaPay-Simulation
A simulation for TandaPay

If you'd like to run the simulation yourself note that the three excel sheets labeled '# User/System Database.xlsx' are required as well as the LOGS file for the program to run as intended.

1. Table of Contents

[TOC]


2. Background

All modern insurance architectures require that a provider hold funds in reserve for paying future claims. Even models that function outside modern insurance principles such as a takaful (risk sharing groups compliant with Islamic law) are required to use custodians who hold reserves for the purpose of paying future claims.  No one has ever seen a working model of insurance that is capable of paying claims that has no custodians and holds no reserves. If it was possible to build a policy using zero-reserve architecture then almost nothing would be known about how these types of architectures would function and what incentive structures would govern the participants. 

TandaPay is a zero-reserve architecture that is optimized to produce groups that collapse when invalid claims are submitted for payment. The TandaPay architecture was created to produce incentive structures that maximize for the attribute of intolerance when it comes to dishonest reports by the members. This makes TandaPay an excellent protocol for whistleblowing software because the threat of collapse should theoretically create a willingness for the group to self-censor in order to maintain its existence. Only claims that are viewed by a super majority (above 90% of participants) as valid should ever be approved for payment.  

Given the assumption that 40% (or more) of the members are honest, the TandaPay protocol can be proven to have the property of group collapse in response to submission of an invalid claim. What is currently unknown is the minimum threshold of honest participants required to produce this type of collapse. If the threshold required to collapse a group can be proven to be very low, then the degree to which the group self-censors claims should be correspondingly very high.

This dynamic can allow entities outside of the community to have a greater sense of certainty as to a claims validity without knowing the contents of a claim. In this way, the architecture, which would threaten to collapse a group for approving an invalid claim is the same architecture that would bolster credibility of the group for approving a valid claim.

What is needed is a simulation that explores different group attributes to determine which architecture is best optimized to produce groups which collapse with the minimum number of honest participants.



3. Background as it pertains to tandaPay

Zero-reserve escrow technology for setting up insurance mutuals is new. In addition to not holding reserves, the architecture permits members to defect against invalid claims. These defections result in a hefty cost upon members who decide to remain in the community. As members leave, premiums can sharply rise, and it is the rise of premiums that can trigger a chain of events that result in group collapse.

There is a potential novelty associated with determining the honesty of an insurance claim using defections. Insurance mutuals have previously not permitted policyholders to leave the group with a refund of their premium, so little is known about this mechanic. A mechanism that permits defectors within the context of a zero-reserve group has never previously been explored by an academic paper.  

Coverage requirements are inflexible demands enforced by smart contracts that claims be paid in full. They mandate that any remaining members make up for the value of premiums that were refunded to defectors. This means that a defectors denial of payment to a claimant requires remaining members to pay an additional cost to make up for this loss.

When coverage requirements are mandated by the system, it causes premiums to increase as members leave the group. Potentially the pairing of these three attributes can produce groups with the property of collapse as a result of a failure to reach consensus on the validity of an insurance claim. It is currently unknown if groups with these attributes can deterministically produce collapse when less than one-third of participants are honest. It is also unknown if there is a threshold of honest participants required to reliably produce collapse.

If it can be shown that the required threshold of a dissenting minority capable of producing group collapse is between 20 to 30% of participants, then the implications related to game theory for determining the honesty of an insurance claim will likely be of profound consequence. The threat of collapse gives the minority an effective means of imposing self-censorship upon the majority. The smaller the minority of honest participants that are required who can effectively prevent a supermajority from colluding to approve an invalid claim, the more an approved claim provides a valuable signal to entities outside of the group. If group collapse (or lack thereof) can become a reliable heuristic (to outsiders) for determining the honesty of an insurance claim then the group has an effective means of generating a historical record that has statistical significance.



4. Goal of THE simulation

It is currently unknown if combining zero-reserve architecture and coverage requirements with a mechanism that permits defections can deterministically produce group collapse when a group's consensus is fractured. If it can be shown that a small dissenting minority can produce sharply rising premiums that effectively result in group collapse, then the implications related to game theory may be of profound consequence. Having an architecture where the threshold of honest participants required to produce collapse is known is likely to be valuable. If TandaPay is one day widely available, models capable of providing the probability that an insurance claim is valid based upon the group's historical record located on the blockchain are therefore also likely to be valuable.

The goal of the simulation is to produce a large and robust data set where multiple variables are evaluated. This data set should correlate architecture with specific starting assumptions to specific group properties. Said another way, the starting assumptions are that smart contracts can enforce inflexible coverage requirements and rising premiums as people defect, skip, or quit (i.e., when a group fractures). Can these starting assumptions be correlated with groups that collapse with a known threshold of honest defectors?

Once correlation is demonstrated, further research may be able to prove a causal relationship between architecture with specific assumptions producing groups with specific properties.



5. What is new about TandaPay

TandaPay uses the blockchain to eliminate third party custodians and the ability for smart contracts to enforce inflexible coverage requirements. Previous research into groups such as broodfonds (breadfunds) and ROSCAs did not focus on the attributes of smart contracts being used to strictly enforce that premiums rise as a result of a fracture. Smart contract inflexibility is generally an underappreciated attribute that TandaPay heavily exploits.

In addition, other approaches did not utilize subgroups. Subgroups are important because they provide novel group dynamics that have also been previously underappreciated such as:



*   The decrease in the signal to noise ratio. Subgroups allow defections to be categorized as either honest or selfish. 
*   This feature is not tested by the simulation, but is part of an initial set of assumptions.
*   Architectures that use subgroups prohibit members from obtaining coverage as individuals; effectively outsourcing the cost of underwriting policies to the group.
*   This feature is not tested by the simulation, but is part of an initial set of assumptions.
*   Architectures that use subgroups accelerate group collapse when consensus is fractured because invalid groups impose costs in terms of morale and increased premiums.
*   The simulation tests this hypothesis.
*   Architectures that use subgroups inhibit members from acting as individuals by effectively imposing a cost associated with selfish defections and removing that same cost for honest defections.
*   This feature is not tested by the simulation, but is part of an initial set of assumptions.
6. Conclusion

The virtue of architecture that can deterministically produce collapse when a group's consensus is fractured is underappreciated. There are thousands of valid configurations for these types of groups. Finding the optimal configuration for collapse will require research, modeling, and the creation of simulations.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")




7. Relationship between ev4 and pv5

The simulation specifies a number of different variables, but the purpose of the simulation is to derive the relationship between the initial number of defectors and the number of members remaining once the group collapses.



    1. Definition of PV5 

Pricing Variable (PV)5 translates premium prices into group collapse. As members leave, premiums rise for the remaining participants. A group is only allowed to lower the cost of their monthly premiums if no members have left the group in the past 30 days as a result of defections, skipped payments, or a failure to reorg (i.e., quit). PV5 specifies a threshold that the group is unable to stop members from skipping out on paying premiums. Although the variable specifies the degree that premiums are required to rise, this can be directly translated to the number of members remaining once the PV5 threshold is crossed by using the following formula:



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



The above formula can be derived from:



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 

or 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



and



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





    2. Definition of EV4

Environmental Variable (EV)4 is the number of members who act as honest defectors at the start of the simulation. If enough members defect in the initial wave, their actions result in a chain of events that can push the group over the PV5 threshold. If this happens, the group is effectively unable to continue.

If the number of members specified in PV4 is insufficient, the group will not cross the PV5 threshold and will be capable of changing their coverage requirement thereby enabling members to lower their premiums and avert group collapse.



8. Input module

[Create user interface for entering in relevant simulation variables]



9. Environmental variables (EV)

Table 1 outlines the EVs used in the simulation and their allowed values.

**_Table 1. Environmental Variables (EVs)_**


<table>
  <tr>
   <td>Variable Name
   </td>
   <td>Variable Definition
   </td>
   <td>Allowed Values
   </td>
  </tr>
  <tr>
   <td>EV1
   </td>
   <td>How many members are in the group?
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>EV2
   </td>
   <td>Average take home pay for group members?
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>EV3
   </td>
   <td>What is the chance of a claim each month?
   </td>
   <td>25 – 75 
   </td>
  </tr>
  <tr>
   <td>EV4
   </td>
   <td>What is the percentage of honest defectors?
   </td>
   <td>10 – 45 
   </td>
  </tr>
  <tr>
   <td>EV5
   </td>
   <td>What is the percentage of low-morale members?
   </td>
   <td>10 – 30 
   </td>
  </tr>
  <tr>
   <td>EV6
   </td>
   <td>What is the percentage of members who are unwilling to act alone?
   </td>
   <td>20 – 80 
   </td>
  </tr>
  <tr>
   <td>EV7
   </td>
   <td>What is the member threshold needed for dependent members to defect?
   </td>
   <td>2, 3, 4
   </td>
  </tr>
  <tr>
   <td>EV8
   </td>
   <td>Poison group for x periods
   </td>
   <td>0, 1, 2, 3
<p>
Default = 3
   </td>
  </tr>
  <tr>
   <td>EV9
   </td>
   <td>Probability a low-morale member will quit if forced to reorg
   </td>
   <td>0.3333
   </td>
  </tr>
  <tr>
   <td>EV10
   </td>
   <td>Coverage requirement
   </td>
   <td>

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 
   </td>
  </tr>
  <tr>
   <td>EV11
   </td>
   <td>Number of remaining members that play a unity role
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>EV12
   </td>
   <td>Number of remaining members that play a role of independent 
   </td>
   <td>
   </td>
  </tr>
</table>




10. Pricing variables (PV)

The following outlines the different PVs used in the simulation, what questions they aim to answer, and their allowed values. 

**Question PV1, PV2, PV3, and PV4 are answering:** What is the premium price sensitivity relative to the previous month?

**PV1 and PV2:** PV1 and PV2 determine the bottom of the threshold, which corresponds to the lowest price impact. The relationship between PV1 and PV2 is as follows:



*   PV1 = <span style="text-decoration:underline;">If</span> the premium price increases by **&lt;insert % between 20 – 40%>** 
*   PV2 = <span style="text-decoration:underline;">Then</span> **&lt;insert % between 1 – 15%>** of policyholders leave

**PV3 and PV4:** PV3 and PV4 determine the top of the threshold, which corresponds to the greatest price impact. The relationship between PV3 and PV4 is as follows:  



*   PV3 = <span style="text-decoration:underline;">If</span> the premium price increases by **&lt;insert % between 30 – 60%>** 
*   PV4 = <span style="text-decoration:underline;">Then</span> **&lt;insert % between 5 – 25%>** of policyholders leave

**Question PV5 and PV6 are answering: **What is the premium price sensitivity relative to pre-facture?



*   PV5 = <span style="text-decoration:underline;">If</span> the premium price increases by **&lt;insert percentage>** 
*   PV6 = <span style="text-decoration:underline;">Then</span> **&lt;insert percentage>** of policyholders leave

**Note: **Auto populate suggestions for PV3 and PV4 based on PV1 and PV2. Suggestions may be modified by the user.



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



**Note: **Auto populate suggestions for PV5 and PV6 based on PV1 and PV2. Suggestions may be modified by the user.



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



**Note: **When automating multiple runs, variables are ranked in order of importance as seen here.



    3. PV Rules

Rules for PVs include the following:



*   PV3 > PV1 <span style="text-decoration:underline;">and</span> PV4 > PV2
*   PV5 > PV3
11. Goal: Create system generator module

Take initial variables as user inputs and use functions to produce database entries as outputs.



    4. Database module

The database module is designed to create, store, and update data using system data and user data.



        1. System Data

System data functions to keep a record of the results and determines what the system will do next. 



*   Period data occupies the rows of the database
*   System record occupies columns of the database
        2. User Data

User data determines what the user will do next.



*   User number occupies rows of the database
*   User record occupies columns of the database
    5. System database

The system database creates 10 periods composed of 30 stages as shown in order below. Stages 5, 8, 11, 14, 17, 20, 23, 26, 29 are not use as a functional part of the simulation.



1. Pay premiums stage for Period 1
2. Finalize claims stage for Period 0
3. Reorg subgroups stage for Period 1
4. Pay premiums stage for Period 2
5. Finalize claims stage for Period 1 
6. Reorg subgroups stage for Period 2
7. Pay premiums stage for Period 3
8. Finalize claims stage for Period 2 
9. Reorg subgroups stage for Period 3
10. Pay premiums stage for Period 4
11. Finalize claims stage for Period 3 
12. Reorg subgroups stage for Period 4
13. Pay premiums stage for Period 5
14. Finalize claims stage for Period 4 
15. Reorg subgroups stage for Period 5
16. Pay premiums stage for Period 6
17. Finalize claims stage for Period 5
18. Reorg subgroups stage for Period 6
19. Pay premiums stage for Period 7
20. Finalize claims stage for Period 6 
21. Reorg subgroups stage for Period 7
22. Pay premiums stage for Period 8
23. Finalize claims stage for Period 7
24. Reorg subgroups stage for Period 8
25. Pay premiums stage for Period 9
26. Finalize claims stage for Period 8
27. Reorg subgroups stage for Period 9
28. Pay premiums stage for Period 10
29. Finalize claims stage for Period 9
30. Reorg subgroups stage for period 10
        3. System record (SyRec) variables

Table 2 provides details regarding the System Record (SyRec) variables. These variables keep track of decisions made by the users. Choices users make have an impact on the cost that a member must pay to continue to receive coverage. As members leave the system record charts the groups progress and enforces that premiums rise in response.

**_Table 2. System Record (SyRec) Variables_**


<table>
  <tr>
   <td>Variable Name
   </td>
   <td>Variable Definition
   </td>
   <td>Initial Values
   </td>
  </tr>
  <tr>
   <td>SyRec1
   </td>
   <td>Valid members remaining
   </td>
   <td>EV1
   </td>
  </tr>
  <tr>
   <td>SyRec2
   </td>
   <td>Premium for a single member
   </td>
   <td>

<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


   </td>
  </tr>
  <tr>
   <td>SyRec3
   </td>
   <td>Number of defected members
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec4
   </td>
   <td>Number of paid members
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec5
   </td>
   <td>Number of members skipped
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec6
   </td>
   <td>Number of invalid members
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec7
   </td>
   <td>Number of members that quit
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec8
   </td>
   <td>Number of reorged members
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec9
   </td>
   <td>Fracture debt from defections
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec10
   </td>
   <td>Fracture debt from skips new
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec11
   </td>
   <td>Fracture debt from skips prior
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec12
   </td>
   <td>Fracture debt from invalid new
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec13
   </td>
   <td>Fracture debt from invalid prior
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec14
   </td>
   <td>Fracture debt total
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec15
   </td>
   <td>Fracture debt per member
   </td>
   <td>No
   </td>
  </tr>
  <tr>
   <td>SyRec16
   </td>
   <td>Claims this period
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec17
   </td>
   <td>Refund value available for new members
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec18
   </td>
   <td>Refund value available for prior members
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>SyRec19
   </td>
   <td>Generic total payment
   </td>
   <td>

<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


   </td>
  </tr>
</table>




    6. User database

The user database consists of a user’s primary and secondary roles and the current status of the user.  These roles and the user’s status determine what decisions they will need to make as the simulation progresses.  



        4. User record (UsRec) variables

Table 3 provides details regarding the User Record (UsRec) variables.

**_Table 3. User Record (UsRec) Variables_**


<table>
  <tr>
   <td>Variable Name
   </td>
   <td>Variable Definition
   </td>
   <td>Initial Values
   </td>
  </tr>
  <tr>
   <td>UsRec1
   </td>
   <td>Original assigned subgroup number
   </td>
   <td>Generated by the subgroup setup
   </td>
  </tr>
  <tr>
   <td>UsRec2
   </td>
   <td>Number of members remaining from original subgroup
   </td>
   <td>Generated by the subgroup setup
   </td>
  </tr>
  <tr>
   <td>UsRec3
   </td>
   <td>Current assigned subgroup number
   </td>
   <td>Generated by the subgroup setup
   </td>
  </tr>
  <tr>
   <td>UsRec4
   </td>
   <td>Number of members in current subgroup
   </td>
   <td>Generated by the subgroup setup
   </td>
  </tr>
  <tr>
   <td>UsRec5
   </td>
   <td>Status of subgroup 
<p>
Accepted values: Valid, Invalid, or NR
   </td>
   <td>Generated by the subgroup setup
   </td>
  </tr>
  <tr>
   <td>UsRec6
   </td>
   <td>Primary role 
<p>
Accepted values: Defector, Low-Morale, or Unity
   </td>
   <td>Generated by the role assignment 
   </td>
  </tr>
  <tr>
   <td>UsRec7
   </td>
   <td>Secondary role
<p>
Accepted values: Dependent or independent
   </td>
   <td>Generated by the role assignment
   </td>
  </tr>
  <tr>
   <td>UsRec8
   </td>
   <td>Current status
<p>
Accepted values: Defected, Paid, Skipped, Paid-Invalid, Quit, Reorg, or NR
   </td>
   <td>Paid
   </td>
  </tr>
  <tr>
   <td>UsRec9
   </td>
   <td>Number of times they have reorged
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>UsRec10
   </td>
   <td>Value of invalid refund available 
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>UsRec11
   </td>
   <td>Total payment specific user
   </td>
   <td>EV1
   </td>
  </tr>
  <tr>
   <td>UsRec12
   </td>
   <td>A member’s ability to pay this period
<p>
Accepted values: Yes, No, or NR
   </td>
   <td>Yes
   </td>
  </tr>
  <tr>
   <td>UsRec13
   </td>
   <td>Defector counter
   </td>
   <td>0
   </td>
  </tr>
</table>




    7. Initialization functions

The simulation utilizes the following initialization functions:



*   Subgroup setup module 
*   Role assignment module
        5. Subgroup setup

**Note: **To see the subgroup setup function performed in Excel, [see this document](https://docs.google.com/spreadsheets/d/1lF42BrWEsvW_A3224bGnQQ0-nhM72QkobPF10YRvvX0/edit?usp=sharing). 

The following steps detail the setup of the subgroup:



1. Start with the total number of members (EV1).
2. Divide the total number of members (EV1) by 5. 
3. Divide the result of Step 2 by 2.3333 and round to the nearest integer.
4. Multiply the result of Step 3 by 5.
5. Subtract the result of Step 4 from Step 1.
6. Divide the remaining members by 6.
7. Divide the result of Step 6 by 2 and round to the nearest integer.
8. Multiply the result of Step 7 by 6.
9. Subtract the result of Step 8 from Step 5.
10. Divide the remaining members by 7.
11. Divide the result of Step 10 by 2 and round down to the nearest integer.
12. Multiply the result of Step 11 by 7.
13. Subtract the result of Step 12 from Step 9.
14. Using the modulo operator, divide the remaining members by 4 and take the result with the remainder.
    1. <span style="text-decoration:underline;">If</span> the remainder from Step 14 = 0, <span style="text-decoration:underline;">then</span> do nothing and continue with Step 15.
    2. <span style="text-decoration:underline;">If</span> the remainder from Step 14 = 1, 2, or 3 members, <span style="text-decoration:underline;">then</span> convert one group of 5 into a group of 6, 7, or 2 groups of 4.
        1. <span style="text-decoration:underline;">If</span> there is a set of 5 member groups, <span style="text-decoration:underline;">then</span> see Step 3 = A
        2. <span style="text-decoration:underline;">If</span> there is a set of 6 member groups, <span style="text-decoration:underline;">then</span> see Step 7 = B
        3. <span style="text-decoration:underline;">If</span> there is a set of 7 member groups, <span style="text-decoration:underline;">then</span> see Step 11 = C
        4. <span style="text-decoration:underline;">If</span> there is a set of 4 member groups, <span style="text-decoration:underline;">then</span> see Step 14 = D
    3. <span style="text-decoration:underline;">If</span> the remainder from Step 14 = 1, <span style="text-decoration:underline;">then</span> set a A - 1 group and a B + 1 group.
    4. <span style="text-decoration:underline;">If</span> the remainder from Step 14 = 2, <span style="text-decoration:underline;">then</span> set a A - 1 group and a C + 1 group.
    5. <span style="text-decoration:underline;">If</span> the remainder from Step 14 = 3, <span style="text-decoration:underline;">then</span> set a A - 1 group and a D + 2 group.
15. Assign a specific subgroup number to each subgroup.
16. Assign the members to each numbered subgroup.
17. Update the user record based on the subgroup setup.
    6. UsRec1 = Assigned in Step 16
    7. UsRec2 = Assigned in Step 16
    8. UsRec3 = Assigned in Step 16
    9. UsRec4 = Assigned in Step 16
    10. UsRec5 = Initially set to Valid
        6. Role assignment

The role assignment consists of 2 roles.


    The 1<sup>st</sup> role consists of EV4, EV5, and EV11.



*   EV4 – What is the percentage of honest defectors?
*   EV5 – What is the percentage of low-morale members?
*   EV11 – The number of remaining members that play a unity role

    The 2<sup>nd</sup> role consists of EV6 and EV12.

*   EV6 – What is the percentage of members who are unwilling to act alone?
*   EV12 – The number of remaining members that play a role of independent

_Instructions for 1<sup>st</sup> role assignment_



1. 

<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

EV4_members with the role of Defector
2. Assign the Defector 1st role to participants at random.
    1. Remove these participants from 1<sup>st</sup> role assignment pool.
3. 

<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 EV5_members** **with the role of Low-Morale
    2. Assign the Low-Morale 1st role to remaining participants at random.
4. Any members who are not assigned a role are assigned with the role of Unity.
5. 

<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



_Instructions for 2<sup>nd</sup> role assignment_



6. 

<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

Initial** **EV6_members** **with the role of Dependent
    3. Assign the Dependent 2nd role to members of any group where UsRec4 = 4.
    4. <span style="text-decoration:underline;">If</span> UsRec4 = 4 > EV6_members**, <span style="text-decoration:underline;">then</span>** stop assigning any members the Dependent role.
    5. <span style="text-decoration:underline;">If</span> UsRec4 = 4 members &lt; EV6_members, <span style="text-decoration:underline;">then</span> assign any remaining EV6_members assignments at random.
7. Assign remaining members the role of Independent.
8. 

<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



_Update user record based on role assignment_



1. Determine the value of UsRec6** **from assigning EV4, EV5, and EV11.
2. Determine the value of UsRec7 from assigning EV6 and EV12.
    8. How funds move through the system

Coverage requirements mandate that the cost of members who defect or skip their premium payments become deficits for any remaining group members. Figure 1 below charts how payments, which were removed by defectors in Function 1, or were never paid by skipped members in Function 2 become accounted for as debt. This debt is then realized as increased premiums calculated in Function 9 and carried forward to the next period by Function 11. If this debt is high enough, it will produce additional members who skip payment of their premiums in Function 2 and the cycle will repeat.



<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.jpg "image_tooltip")


**_Figure 1. How Defections Generate Group Debt_**

If a group has no claims in a given month, the premiums must be returned to members as refunds. The process of returning premiums back to members takes about one month before these refunds become available to lower the cost of future premiums. As show in Figure 2 below, Function 8 determines if the current period has a claim, and Function 11 moves that credit forward into the next period. Finally, the credit reduces the members premiums in Function 2 and thus the likelihood that members will skip payment of their premium.



<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.jpg "image_tooltip")


**_Figure 2. How Refunds Generate Credits_**



    9. System and user functions module

The following sections explain the system and user functions module. The functions and database work together by utilizing the following:



*   Most system or user functions evaluate the user record row by row.
*   The function then modifies the user record if certain conditions are met. This modification may also result in a modification of the system record.
*   Once all the rows of the user record are completely evaluated, move to the next function.
*   The functions move from the Pay Stage to the Finalize Stage and then the Reorg Stage.
*   When all stages are complete, advance to the next period in the system record.
        1. System and user function breakdown

The following includes a step-by-step breakdown of the system and user functions module. 



**UsFunc1 Detailed Description**

**Function name: **UsFunc1 – User defection function

**Stage and period: **Pay Stage 1 – Only run for Period 1


    **UsFunc1 input:** UsRec1, UsRec6, UsRec7, and EV7

**Initial check:** Is the simulation currently on Period 1?



*   <span style="text-decoration:underline;">If</span> yes, <span style="text-decoration:underline;">then</span> continue.
*   <span style="text-decoration:underline;">If</span> no, ?

_Path 0_



1. Path 0 start. Load user record. 
2. Count total users in user record = &lt;end of user list>** **
3. Start with user &lt;**current user #>**.
    1. <span style="text-decoration:underline;">If</span> user &lt;**current user #> **= Defector, <span style="text-decoration:underline;">then</span> continue to Path 0.5.
    2. <span style="text-decoration:underline;">Else if</span>, **&lt;current user #>** = **&lt;end of user list>**, <span style="text-decoration:underline;">then</span> continue to Path 1.5.
    3. <span style="text-decoration:underline;">Else</span>, move to **&lt;current user #> + 1** and go to Path 0 start.

_Path 0.5_



*   <span style="text-decoration:underline;">If</span> user **&lt;current user #>** UsRec7 = Dependent, <span style="text-decoration:underline;">then</span> evaluate Path 1.
    *   <span style="text-decoration:underline;">Else</span>, add to Path 2 Run Set. 
*   <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of user list>**, <span style="text-decoration:underline;">then</span> continue to Path 1.5.
    *   <span style="text-decoration:underline;">Else</span>, move to **&lt;current user #> + 1** and go to Path 0 start.

_Path 1_



1. For all users where UsRec6 = Defector and UsRec7 = Dependent, 
    1. Read **&lt;current user #>** UsRec3 = Load into **&lt;GroupRead>**.
2. For every user where UsRec3 = **&lt;GroupRead>**,
    2. Increment UsRec13 by 1.
3. Clear **&lt;GroupRead>**.
4. <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of user list>**, <span style="text-decoration:underline;">then</span> continue to Path 1.5.
5. <span style="text-decoration:underline;">Else</span>, move to **&lt;current user #> + 1** and go to Path 0 start.

_Path 1.5_



*   For all users where UsRec6 = Defector and UsRec7 = Dependent,
    *   <span style="text-decoration:underline;">If</span> UsRec13 ≥ EV7, <span style="text-decoration:underline;">then</span> add to Path 2 Run Set.
    *   Else, add to Path 3 run set, then load Path 2 Run Set. 

_Path 2 Run Set_



1. Decrement SyRec1 by 1.
2. Defecting for previous period.
    1. Increment SyRec3 by 1.
3. Skipping for current period.
    2. Increment SyRec5 by 1.
4. Referencing UsRec3, 
    3. Decrease UsRec4 by 1 for <span style="text-decoration:underline;">all</span> users with same UsRec3 value.
    4. Decrease UsRec2 by 1 for <span style="text-decoration:underline;">all</span> users with same UsRec1 <span style="text-decoration:underline;">and</span> UsRec3.
        1. UsRec3 = 0
        2. UsRec4 = 0
        3. UsRec5 = NR
        4. UsRec8 = NR
        5. UsRec12 = NR

_Path 3 Run Set_



1. Load Path 3 Run Set.
2. For all users in Path 3 Run Set,
    1. UsRec6 = Low-Morale
3. Continue to Path 4.

_Path 4_



1. Clear Path 2 Run Set.
2. Clear Path 3 Run Set.
3. Continue to UsFunc2.



**UsFunc2 Detailed Description**

**Function name: **UsFunc2 – User skip function

**Stage: **Pay Stage 2

**UsFunc2 workflow: **The workflow of UsFunc2 is shown below in Figure 3.



<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


**_Figure 3. Workflow of UsFunc2_**

**At start of simulation:** PV1, PV2, PV3, and PV4



*   Find the slope of price sensitivity relative to the previous month.
*   

<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



**Note:** The y-axis represents the percentage of people who will skip their premiums. The x-axis represents the amount (in percent) that the premium price has increased.

_Run each period_

**Initial check:** Is the simulation currently on Period 1?



*   <span style="text-decoration:underline;">If</span> yes, <span style="text-decoration:underline;">then</span> end the function.
*   <span style="text-decoration:underline;">If</span> no, <span style="text-decoration:underline;">then</span> continue. 

**UsFunc2 input:** SyRec19 for the current period pay stage and SyRec19 for the previous period pay stage.



*   a = SyRec19 for the current period pay stage
*   b = SyRec19 for the previous period pay stage
*   

<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

= % Increase in Premiums
*   <span style="text-decoration:underline;">If</span> % Increase in Premiums &lt; PV1, <span style="text-decoration:underline;">then</span> continue to Path 2
*   <span style="text-decoration:underline;">If</span> % Increase in Premiums ≥ PV1, <span style="text-decoration:underline;">then</span> continue to Path 1

_Path 1_



*   

<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 where:
    *   

<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


    *   

<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


    *   y = Skip% = Percent of users who will skip 

**Path 1 input:** SyRec1 and Skip%

**Path 1 Output:** Skip#



1. Identify group where UsRec5 = Valid.
2. Randomly select (Skip#) number of users where UsRec5 = Valid.
3. Group of skip users = Set of users.
4. Set of users UsRec12 = No.

_Path 2_



1. <span style="text-decoration:underline;">If</span> 

<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

&lt; PV5, <span style="text-decoration:underline;">then</span> continue to Path 3.
2. <span style="text-decoration:underline;">If</span> 

<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

≥ PV5, <span style="text-decoration:underline;">then</span> determine Skip# to the nearest whole number.
    1. 

<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


3. Identify group where UsRec5 = Valid.
4. Randomly select (Skip#) number of users where UsRec5 = Valid.
5. Group of skip users = Set of users.
6. Set of users UsRec12 = No

_Path 3_



1. <span style="text-decoration:underline;">If</span> EV8 = 0, <span style="text-decoration:underline;">then</span> do nothing.
2. <span style="text-decoration:underline;">If</span> EV8 = 1, 2, or 3, <span style="text-decoration:underline;">then</span> decrease EV8 by 1.
    1. At random, select 1 user record where UsRec5 = Valid.
    2. Update user.
    3. UsRec12 = No

**Note: **Once Path 1, Path 2, and Path 3 are completed for all records, continue to SyFunc3.



**SyFunc3 Detailed Description**

**Function name: **SyFunc3 – Validate premium function

**Stage: **Pay Stage 3

**Input:** UsRec12

_Path 0 Initialization _



1. Load user record.
2. Create user list from user record where UsRec5 = Valid.
3. Count users in list = **&lt;end of user list>**.
4. Load user list. 
5. Start with first user in user list **&lt;current user #>**.
6. Continue to Path 0 Start.

_Path 0 Start_



1. Evaluate user **&lt;current user #>**.
2. <span style="text-decoration:underline;">If</span> UsRec12 = No, <span style="text-decoration:underline;">then</span> update UsRec8 = Skipped and add to Path 1 Run Set.
    1. <span style="text-decoration:underline;">Else</span> (UsRec12 must be yes), update UsRec8 = Paid.
3. <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of user list>**, then load Path 1.
    2. <span style="text-decoration:underline;">Else</span>, move to **&lt;current user #> + 1 **and go to Path 0 Start.

_Path 1 _



1. If UsRec12 = No, <span style="text-decoration:underline;">then</span> complete the following: 
    1. Update UsRec8 = Skipped.
    2. Decrement SyRec1 by 1.
    3. Increment SyRec5 by 1.
    4. Referencing UsRec3, 
        1. Decrease UsRec4 by 1 for <span style="text-decoration:underline;">all</span> users with same UsRec3 value.
        2. Decrease UsRec2 by 1 for <span style="text-decoration:underline;">all</span> users with same UsRec1 <span style="text-decoration:underline;">and</span> UsRec3.
2. UsRec3 = 0
3. UsRec4 = 0
4. UsRec5 = NR
5. UsRec8 = NR
6. UsRec12 = NR

_Path 2_



1. Clear Path 1 Run Set.
2. Continue to SyFunc4.

**SyFunc4 Detailed Description**

**Function name: **SyFunc4 – Invalidate subgroup function

**Stage:** Pay Stage 4

**SyFunc4 input: **UsRec4, UsRec8, and UsRec11



*   <span style="text-decoration:underline;">If</span> UsRec4 = 1, 2, or 3 <span style="text-decoration:underline;">and</span> UsRec8 = Paid, <span style="text-decoration:underline;">then</span> complete the following:
    *   Assign UsRec8 = Paid-Invalid					
    *   Assign UsRec5 = Invalid						
    *   Assign UsRec10 = UsRec11
    *   Increase SyRec6 by 1
    *   Continue to Path 1.
*   <span style="text-decoration:underline;">If</span> UsRec4 = 4, 5, 6, or 7, <span style="text-decoration:underline;">then</span> continue to Path 1.				

_Path 1_

**Initial check: **Is the simulation currently on Period 1?



*   <span style="text-decoration:underline;">If</span> yes, <span style="text-decoration:underline;">then</span> advance to SyFunc5.
    *   Advance (copy) values in current System Record row to finalize stage Period 0.
*   <span style="text-decoration:underline;">If</span> no, <span style="text-decoration:underline;">then</span> period = x advance to SyFunc6
    *   Advance (copy) values in current System Record row to Reorg Stage Period x row.



**SyFunc5 Detailed Description**

**Function name: **SyFunc5 – Finalize premium function

**Stage and period: **Finalize Stare – only run for Period 0

**Initial check: **Is the simulation currently on Period 0?



*   <span style="text-decoration:underline;">If</span> yes, <span style="text-decoration:underline;">then</span> continue to SyFunc5 input.
*   <span style="text-decoration:underline;">Else</span>, <span style="text-decoration:underline;">then</span> do nothing.

**SyFunc5 input:** UsRec8 = Defected



*   <span style="text-decoration:underline;">If</span> UsRec8 = Defected, <span style="text-decoration:underline;">then</span> increase SyRec3 by 1.
*   <span style="text-decoration:underline;">Otherwise</span>, do nothing.

**SyFunc5 output: **SyRec9



1. Calculate SyRec9.
    6. 

<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


2. Advance values in current System Record row to Reorg Stage Period 1 row.
3. Advance to UsFunc6.



**UsFunc6 Detailed Description**

**Function name: **UsFunc6 – User quit function

**UsFunc6 workflow: **The workflow of UsFunc6 is shown below in Figure 4.



<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


**_Figure 4. UsFunc6 Workflow_**

_Path 0 Initialization_



1. Load user record.
2. Create user list from user record where UsRec8 = Paid-Invalid.
    1. Count users in list = **&lt;end of user list>**.
3. Load user list.
    2. Start with first user in user list **&lt;current user #>**.

_Path 0 Start_



*   Evaluate &lt;current user #>.
    *   <span style="text-decoration:underline;">If</span> user **&lt;current user #>** UsRec6 = Low-Morale, <span style="text-decoration:underline;">then</span> add to Path 1 Run Set. 
        *   <span style="text-decoration:underline;">Else</span>, add to Path 3 Run Set
    *   <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of user list>**, then load Path 1. 
        *   <span style="text-decoration:underline;">Else</span>, continue to **&lt;current user #>** + 1 and go to Path 0 Start.

_Path 1_



1. Load Path 1 Run Set.
2. For <span style="text-decoration:underline;">all</span> users where UsRec6 = Low-Morale <span style="text-decoration:underline;">and</span> UsRec8 = Paid-Invalid,
    1. Count users in set = **&lt;end of path 1 set list>**.
3. Continue Path 1 User Evaluation.

_Path 1 User Evaluation_



1. Start with user **&lt;current user # path 1>** in set Path 1 Run Set.
2. Calculate a random number in the range of 0 to 1 = **&lt;probability>**.
    1. <span style="text-decoration:underline;">If</span> **&lt;probability> **≥ EV9, <span style="text-decoration:underline;">then</span> add user to Path 3 Set List.
        1. Else, add user to Path 2a Set List and update UsRec8 = Quit.
3. <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of path 1 set list>**, <span style="text-decoration:underline;">then</span> load Path 2a.
    2. <span style="text-decoration:underline;">Else</span>, increment value for **&lt;current user # path 1>** by 1 in set Path 1 Run.
4. Clear **&lt;probability>**.
5. Go to Path 1 User Evaluation.

_Path 2a_



1. Load Path 2a Run Set list.
2. For all users where UsRec8 = Quit,
    1. Count users in set = **&lt;end of path 2 set list>**.
3. For each user in Path 2 Run Set.
    2. Decrement SyRec1 by 1.
    3. Increment SyRec 7 by 1
4. Continue to Path 2a User Evaluation.

_Path 2a User Evaluation_



1. Start with user **&lt;current user # path 2>** in set Path 2 Run Set list.
2. Read **&lt;current user #>** UsRec3 = Load into **&lt;GRead A>**.
3. Read **&lt;current user #>** UsRec1 = Load into **&lt;GRead B>**.
4. For every user in record where UsRec3 = **&lt;GRead A>**,
    1. Decrease UsRec4 by 1.
5. For every user in record where UsRec3 = **&lt;GRead A>** <span style="text-decoration:underline;">and</span> UsRec1 = **&lt;GRead B>**,
    2. Decrease UsRec2 by 1.
6. Assign the current values for **&lt;current user # path 2> **as follows:
    3. UsRec3 = 0
    4. UsRec4 = 0
    5. UsRec5 = NR
    6. UsRec8 = NR
    7. UsRec12 = NR
7. <span style="text-decoration:underline;">If</span> **&lt;current user # path 2>** = **&lt;end of path 2 set list>**, <span style="text-decoration:underline;">then</span>
    8. Clear **&lt;GRead A>**,
    9. Clear **&lt;GRead B>**, 
    10. Clear Path 2 Run Set, and
    11. Continue to Path 3.
    12. <span style="text-decoration:underline;">Else</span>, increment value for **&lt;current user # path 2>** by 1 in set Path 2a Run Set,
    13. Clear **&lt;GRead A>**,
    14. Clear **&lt;GRead B>**, and 
    15. Go to Path 2a User Evaluation.

_Path 3_



1. Load Path 3 Set List.
2. Count users in set = **&lt;end of path 3 set list>**.

_Path 3 User Evaluation_



1. Evaluate user **&lt;current user # path 3 set list>**.
    1. <span style="text-decoration:underline;">If</span> user **&lt;current user #>** UsRec7 = Dependent, <span style="text-decoration:underline;">then</span> evaluate the following:
        1. <span style="text-decoration:underline;">If</span> UsRec2 ≥ 2, <span style="text-decoration:underline;">then</span> add user to Path 4 Set List.
        2. <span style="text-decoration:underline;">Else</span>, add user to Path 2b Set List and update UsRec8 = Quit.
    2. <span style="text-decoration:underline;">Else</span> (UsRec7 = Independent), <span style="text-decoration:underline;">then</span> add user to Path 4 Set List.
2. Then,
    3. <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of path 3 set list>**, <span style="text-decoration:underline;">then</span> go to Path 2b.
    4. <span style="text-decoration:underline;">Else</span>, continue to **&lt;current user #>** + 1 and go to Path 3 User Evaluation.

_Path 2_



1. Decrement SyRec1 by 1.
2. Increment SyRec7 by 1.
3. Referencing UsRec3, 
    1. Decrease UsRec4 by 1 for <span style="text-decoration:underline;">all</span> users with same UsRec3 value.
    2. Decrease UsRec2 by 1 for <span style="text-decoration:underline;">all</span> users with same UsRec 1 <span style="text-decoration:underline;">and</span> UsRec3.
4. <span style="text-decoration:underline;">If</span> UsRec8 = Quit, <span style="text-decoration:underline;">then</span>:
    1. UsRec3 = 0
    2. UsRec4 = 0
    3. UsRec5 = NR
    4. UsRec8 = NR
    5. UsRec12 = NR
5. Continue to Path 2b User Evaluation.

_Path 2b User Evaluation_



1. Start with user **&lt;current user # path 2>** in set Path 2b Run Set.
2. Read **&lt;current user #>** UsRec3 = Load into **&lt;GRead A>**.
3. Read **&lt;current user #>** UsRec1 = Load into **&lt;GRead B>**.
4. For every user in record where UsRec3 = **&lt;GRead A>**, decrease UsRec4 by 1.
5. For every user in record where UsRec 3 = &lt;GRead A> and UsRec 1 = &lt;GRead B>, decrease UsRec2 by 1.
6. Assign the current values for &lt;current user # path 2> as follows:
    1. UsRec3 = 0
    2. UsRec4 = 0
    3. UsRec5 = NR
    4. UsRec8 = NR
    5. UsRec12 = NR
7. <span style="text-decoration:underline;">If</span> **&lt;current user # path 2>** = **&lt;end of path 2 set list>**, <span style="text-decoration:underline;">then</span>
    6. Clear **&lt;GRead A>**,
    7. Clear **&lt;GRead B>**,
    8. Clear Path 2 Run Set, and 
    9. Continue to Path 4.
8. <span style="text-decoration:underline;">Else</span>, increment value for **&lt;current user # path 2>** by 1 in set Path 2b Run Set,
    10. Clear **&lt;GRead A>**,
    11. Clear **&lt;GRead B>**, and
    12. Go to Path 2b User Evaluation.

_Path 4_



1. Load Path 4 Set List.
2. Count users in set = **&lt;path 4 set list>**.
3. For all users in Path 4 Set List,
    1. Increment SyRec8 by 1.
    2. Check if UsRec8 = Paid-Invalid.
        1. <span style="text-decoration:underline;">If</span> UsRec8 ≠ Paid-Invalid, <span style="text-decoration:underline;">then</span> throw error and terminate.
    3. Check if UsRec2 ≥ 2.
        2. <span style="text-decoration:underline;">If </span>UsRec2 &lt; 2, <span style="text-decoration:underline;">then</span> throw error and terminate. 
4. Clear Path 2 Run Set.
5. Clear Path 3 Run Set.
6. Continue to SyFunc7.



**SyFunc7 Detailed Description**

**Function name:** SyFunc7 – Reorg user function

**Stage:** Reorg Stage 2 

**SyFunc7 workflow: **The workflow of SyFunc7 is shown below in Figure 5.



<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


**_Figure 5. SyFunc7 Workflow_**

_Path 0 Initialization _



1. Load user record.
2. Create user list from user record where UsRec8 = Paid-Invalid.
    1. Count users in list = **&lt;end of user list>**.
3. Load user list.
4. Start with first user in user list **&lt;current user #>**.

_Path 0 Start_



1. Evaluate **&lt;current user #>**.
    1. <span style="text-decoration:underline;">If</span> user **&lt;current user #>** UsRec4 = 1, <span style="text-decoration:underline;">then</span> add to Path 1 Run Set.
    2. <span style="text-decoration:underline;">Else</span>, continue.
    3. <span style="text-decoration:underline;">If</span> user **&lt;current user #>** UsRec4 = 2, <span style="text-decoration:underline;">then</span> add to Path 2 Run Set.
    4. <span style="text-decoration:underline;">Else</span>, continue.
    5. <span style="text-decoration:underline;">If</span> user **&lt;current user #>** UsRec4 = 3, <span style="text-decoration:underline;">then</span> add to Path 3 Run Set.
    6. <span style="text-decoration:underline;">Else</span>, throw error if UsRec4 = 4, 5, 6, or 7, and terminate.
2. <span style="text-decoration:underline;">If</span> **&lt;current user #>** = **&lt;end of user list>**, <span style="text-decoration:underline;">then</span> load Path 1.
3. <span style="text-decoration:underline;">Else</span>, continue to **&lt;current user #>** + 1 and go to Path 0 Start.

_Path 1_

**Path 1 First Attempt**



1. For <span style="text-decoration:underline;">all</span> users where UsRec4 = 1,
    1. Load Path 1 Run Set.
    2. Create a list from set.
        1. Add all UsRec3 values to **&lt;P1 UsRec3 invalid list>**.
        2. Eliminate all duplicates.
2. Load user record.
3. Filter records that satisfy the following requirements:
    3. User record UsRec5 = Valid and user record UsRec4 = 6.
    4. Create a list from record. 
        3. Add all UsRec3 values to **&lt;P1 UsRec3 valid list>**.
        4. Eliminate all duplicates.

**Path 1 Assignment First Attempt**



1. Start at current entry on list **&lt;P1 UsRec3 invalid list>**.
2. Current entry = **&lt;UsRec3 NeedMatch>**.
3. Match with random entry from **&lt;P1 UsRec3 valid list>** = **&lt;UsRec3 GiveMatch>**.
4. Find users from Path 1 Run Set where UsRec3 = **&lt;UsRec3 NeedMatch>**.
5. Update with the following values:
    1. UsRec3 = &lt;UsRec3 GiveMatch>
    2. UsRec4 = 7
    3. UsRec5 = Valid
    4. UsRec8 = Reorg
    5. UsRec9 = UsRec9 + 1
6. Remove:
    6. Entry on **&lt;P1 UsRec3 invalid list>** where UsRec3 = **&lt;UsRec3 NeedMatch> **and
    7. Users from Path 1 Run Set where UsRec3 = **&lt;UsRec3 NeedMatch>**.
7. Find users from user record where UsRec3 = **&lt;UsRec3 GiveMatch>**.
8. Assign UsRec4 = 7.
9. Remove entry on **&lt;P1 UsRec3 valid list>** where UsRec 3 = **&lt;UsRec3 GiveMatch>**.
10. Reset **&lt;UsRec3 GiveMatch>** and **&lt;UsRec3 NeedMatch>**.
11. <span style="text-decoration:underline;">If</span> **&lt;P1 UsRec3 invalid list>** is empty, <span style="text-decoration:underline;">then</span> check if Path 1 Run Set is empty.
    8. <span style="text-decoration:underline;">If </span>Path 1 Run Set is empty, <span style="text-decoration:underline;">then</span> clear **&lt;P1 UsRec3 valid list>** and continue to Path 2.
    9. <span style="text-decoration:underline;">Else</span>, throw an error.
12. <span style="text-decoration:underline;">Else</span>, check if **&lt;P1 UsRec3 valid list>** is empty.
    10. <span style="text-decoration:underline;">If</span> **&lt;P1 UsRec3 valid list>** is empty, then try Path 1 Second Attempt. 
    11. <span style="text-decoration:underline;">Else</span>, return to Path 1 Assignment First Attempt.

**Path 1 Second Attempt**



1. Load user record.
2. Filter records that satisfy the following requirements:
    1. User record UsRec5 = Valid and
    2. User record UsRec4 = 5.
3. Create a list from record. 
    3. Add <span style="text-decoration:underline;">all</span> UsRec3 values to **&lt;P1 UsRec3 valid list>**.
    4. Eliminate all duplicates.

**Path 1 Assignment Second Attempt**

Start at current entry on list &lt;P1 UsRec 3 invalid list> 

   Current entry = &lt;UsRec3 NeedMatch>

   Match with random entry from &lt;P1 UsRec 3 valid list> = &lt;UsRec3 GiveMatch>

     Find users from path 1 run set where

       UsRec 3 = &lt;UsRec3 NeedMatch>

     Update with the following values:

UsRec 3 = &lt;UsRec3 GiveMatch>

UsRec 4 = 6

UsRec 5 = valid

UsRec 8 = reorg

UsRec 9 = increment by 1

Then 

     Remove

       Entry on &lt;P1 UsRec 3 invalid list> where

         UsRec 3 = &lt;UsRec3 NeedMatch> 

       Users from path 1 run set where

         UsRec 3 = &lt;UsRec3 NeedMatch>

Then 

    Find users from User Record where

   UsRec 3 = &lt;UsRec3 GiveMatch>

Update

   UsRec 4 = 6

Then

    Remove

       Entry on &lt;P1 UsRec 3 valid list> where

         UsRec 3 = &lt;UsRec3 GiveMatch>

Then    

     Reset

        &lt;UsRec3 GiveMatch>

        &lt;UsRec3 NeedMatch>

Then

  If &lt;P1 UsRec 3 invalid list> is empty

    Then

      Check if path 1 run set is empty

        If empty 

           then clear &lt;P1 UsRec 3 valid list>

           proceed to path 2

       Else throw error

  Else

    Else return to Path 1 Assignment second attempt

Path 2

Path 2 first attempt

For all users where UsRec 4 = 2 

Load path 2 run set

Create a list from set

  Add all UsRec 3 values to &lt;P2 UsRec 3 invalid list>

  Eliminate all duplicates

Then

Load user record

Filter records which satisfy the requirement

    User record UsRec 5 = valid

    User record UsRec 4 = 5

  Create a list from record 

    Add all UsRec 3 values to &lt;P2 UsRec 3 valid list>

    Eliminate all duplicates

Path 2 Assignment first attempt

Start at current entry on list &lt;P2 UsRec 3 invalid list> 

   Current entry = &lt;UsRec3 NeedMatch>

   Match with random entry from &lt;P2 UsRec 3 valid list> = &lt;UsRec3 GiveMatch>

     Find users from path 2 run set where

       UsRec 3 = &lt;UsRec3 NeedMatch>

     Update with the following values:

UsRec 3 = &lt;UsRec3 GiveMatch>

UsRec 4 = 7

UsRec 5 = valid

UsRec 8 = reorg

UsRec 9 = increment by 1

Then 

     Remove

       Entry on &lt;P2 UsRec 3 invalid list> where

         UsRec 3 = &lt;UsRec3 NeedMatch> 

       Users from path 2 run set where

         UsRec 3 = &lt;UsRec3 NeedMatch>

Then 

    Find users from User Record where

   UsRec 3 = &lt;UsRec3 GiveMatch>

Update

   UsRec 4 = 7

Then

    Remove

       Entry on &lt;P2 UsRec 3 valid list> where

         UsRec 3 = &lt;UsRec3 GiveMatch>

Then    

     Reset

        &lt;UsRec3 GiveMatch>

        &lt;UsRec3 NeedMatch>

Then

  If &lt;P2 UsRec 3 invalid list> is empty

     Check if path 2 run set is empty

        If empty 

           then clear &lt;P2 UsRec 3 valid list>

           proceed to path 3

       Else throw error

  Else

    Check if &lt;P2 UsRec 3 valid list> is empty

      If empty

        Then try Path 2 second attempt

      Else return to Path 2 Assignment first attempt

Path 2 second attempt

Load user record

Filter records which satisfy the requirement

    User record UsRec 5 = valid

    User record UsRec 4 = 4

  Create a list from record 

    Add all UsRec 3 values to &lt;P2 UsRec 3 valid list>

    Eliminate all duplicates

Path 2 Assignment second attempt

Start at current entry on list &lt;P2 UsRec 3 invalid list> 

   Current entry = &lt;UsRec3 NeedMatch>

   Match with random entry from &lt;P2 UsRec 3 valid list> = &lt;UsRec3 GiveMatch>

     Find users from path 2 run set where

       UsRec 3 = &lt;UsRec3 NeedMatch>

     Update with the following values:

UsRec 3 = &lt;UsRec3 GiveMatch>

UsRec 4 = 6

UsRec 5 = valid

UsRec 8 = reorg

UsRec 9 = increment by 1

Then 

     Remove

       Entry on &lt;P2 UsRec 3 invalid list> where

         UsRec 3 = &lt;UsRec3 NeedMatch> 

       Users from path 2 run set where

         UsRec 3 = &lt;UsRec3 NeedMatch>

Then 

    Find users from User Record where

   UsRec 3 = &lt;UsRec3 GiveMatch>

Update

   UsRec 4 = 6

Then

    Remove

       Entry on &lt;P2 UsRec 3 valid list> where

         UsRec 3 = &lt;UsRec3 GiveMatch>

Then    

     Reset

        &lt;UsRec3 GiveMatch>

        &lt;UsRec3 NeedMatch>

Then

  If &lt;P2 UsRec 3 invalid list> is empty

    Then

      Check if path 2 run set is empty

        If empty 

           then clear &lt;P2 UsRec 3 valid list>

           proceed to path 3

       Else throw error

  Else

    Else return to Path 2 Assignment second attempt

Path 3

Path 3 first attempt

For all users where UsRec 4 = 3 

Load path 3 run set

Create a list from set

  Add all UsRec 3 values to &lt;P3 UsRec 3 invalid list>

  Eliminate all duplicates

Then

  If set has two or more values

    goto Path 3 assignment first attempt

  Else

    Goto Path 3 assignment second attempt

Path 3 Assignment first attempt

Start at current entry on list &lt;P3 UsRec 3 invalid list> 

   Current entry = &lt;UsRec3 NeedMatch>

   Match with next entry from &lt;P3 UsRec 3 invalid list> = &lt;UsRec3 GiveMatch>

     Find users from path 3 run set where

       UsRec 3 = &lt;UsRec3 NeedMatch>

     Update with the following values:

UsRec 3 = &lt;UsRec3 GiveMatch>

UsRec 4 = 6

UsRec 5 = valid

UsRec 8 = reorg

UsRec 9 = increment by 1

Then 

     Remove

       Entry on &lt;P3 UsRec 3 invalid list> where

         UsRec 3 = &lt;UsRec3 NeedMatch> 

       Users from path 3 run set where

         UsRec 3 = &lt;UsRec3 NeedMatch>

Then 

    Find users from User Record where

   UsRec 3 = &lt;UsRec3 GiveMatch>

Update

   UsRec 4 = 6

   UsRec 5 = valid

UsRec 8 = reorg

UsRec 9 = increment by 1

Then

    Remove

       Entry on &lt;P3 UsRec 3 invalid list> where

         UsRec 3 = &lt;UsRec3 GiveMatch>

       Users from path 3 run set where

         UsRec 3 = &lt;UsRec3 GiveMatch>

Then    

     Reset

        &lt;UsRec3 GiveMatch>

        &lt;UsRec3 NeedMatch>

Then

  If &lt;P3 UsRec 3 invalid list> is empty

     Check if path 3 run set is empty

        If empty 

           END FUNCTION

       Else throw error

  Else

    Check if &lt;P3 UsRec 3 invalid list> has two or more values

      If two or more values

        return to Path 3 Assignment first attempt

      Else goto try Path 3 second attempt

Path 3 second attempt

Load user record

Filter records which satisfy the requirement

    User record UsRec 5 = valid

    User record UsRec 4 = 4

  Create a list from record 

    Add all UsRec 3 values to &lt;P3 UsRec 3 valid list>

    Eliminate all duplicates

Path 3 Assignment second attempt

Start at current entry on list &lt;P3 UsRec 3 invalid list> 

   Current entry = &lt;UsRec3 NeedMatch>

   Match with random entry from &lt;P3 UsRec 3 valid list> = &lt;UsRec3 GiveMatch>

     Find users from path 3 run set where

       UsRec 3 = &lt;UsRec3 NeedMatch>

     Update with the following values:

UsRec 3 = &lt;UsRec3 GiveMatch>

UsRec 4 = 7

UsRec 5 = valid

UsRec 8 = reorg

UsRec 9 = increment by 1

Then 

     Remove

       Entry on &lt;P3 UsRec 3 invalid list> where

         UsRec 3 = &lt;UsRec3 NeedMatch> 

       Users from path 3 run set where

         UsRec 3 = &lt;UsRec3 NeedMatch>

Then 

    Find users from User Record where

   UsRec 3 = &lt;UsRec3 GiveMatch>

Update

   UsRec 4 = 7

Then

    Remove

       Entry on &lt;P3 UsRec 3 valid list> where

         UsRec 3 = &lt;UsRec3 GiveMatch>

Then    

     Reset

        &lt;UsRec3 GiveMatch>

        &lt;UsRec3 NeedMatch>

Then

  If &lt;P3 UsRec 3 invalid list> is empty

    Then

      Check if path 3 run set is empty

        If empty 

           then clear &lt;P3 UsRec 3 valid list>

           END FUNCTION

       Else throw error

  Else

    Check if &lt;P3 UsRec 3 valid list> is empty

      If empty

        throw error

      Else return to Path 3 Assignment second attempt

**SyFunc8 Detailed Description**

**Function name: **SyFunc8 – Claims/refunds function

**Stage: **Reorg Stage 4

**SyFunc8 input:** EV3 and the Period Number

Evaluate the period number as follows:



*   <span style="text-decoration:underline;">If</span> the Period Number = 0, <span style="text-decoration:underline;">then</span> end the function.
*   <span style="text-decoration:underline;">If</span> the Period Number ≠ 0, <span style="text-decoration:underline;">then</span> continue SyFunc8.
1. Calculate the probability of SyRec16 (Boolean), given EV3 as follows: 
    1. <span style="text-decoration:underline;">If</span> no, <span style="text-decoration:underline;">then</span> write SyRec2 to SyRec17.
    2. <span style="text-decoration:underline;">If</span> yes, <span style="text-decoration:underline;">then</span> do nothing.
2. Continue to SyFunc9.



**SyFunc9 Detailed Description**

**Function name:** SyFunc9 – Pricing function

**Stage: **Reorg Stage 5



1. Calculate SyRec2.
    1. 

<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


2. Calculate SyRec14.
    2. 

<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


3. Calculate SyRec15.
    3. 

<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


4. Calculate UsRec11.
    4. 

<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 <span style="text-decoration:underline;">or </span>

<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


    5. <span style="text-decoration:underline;">If </span>UsRec10 is used to calculate UsRec11, <span style="text-decoration:underline;">then</span> assign UsRec10 = 0 <span style="text-decoration:underline;">after</span> calculating UsRec11. 
5. Calculate SyRec19.
    6. 

<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


6. Continue to SyFunc10.

**Note:** SyFunc9 provides output for individual user.

**Note:** The ability to calculate UsRec11 using two different methods prevents the same refund from being counted twice.

**Note:** Setting UsRec10 = 0 after UsRec10 is used to calculate UsRec11 prevents the same refund from being counted twice.



**SyFunc10 Detailed Description**

**Function name: **SyFunc10 – Account for fracture debt (Invalid or Skipped)

**Stage: **Reorg Stage 6



1. Calculate SyRec10.
    1. 

<p id="gdcalert38" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert39">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


2. Calculate SyRec12.
    2. 

<p id="gdcalert39" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert40">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


3. Continue to SyFunc11.



**SyFunc11 Detailed Description**

** Function name: **SyFunc11 – Advance period

**Stage: **Reorg Stage 7

**Initial check:** Is the current period 10?



*   <span style="text-decoration:underline;">If</span> the current period = 10, <span style="text-decoration:underline;">then</span> terminate and continue to **Path 2**.
*   <span style="text-decoration:underline;">If</span> the current period ≠ 10, <span style="text-decoration:underline;">then</span> continue.
1. Calculate Total.
    1. 

<p id="gdcalert40" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert41">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


2. <span style="text-decoration:underline;">If</span> Total > 0, <span style="text-decoration:underline;">then</span> continue to Path 1.
3. <span style="text-decoration:underline;">If</span> Total = 0, <span style="text-decoration:underline;">then</span> terminate and continue to Path 2.

_Path 1_

**Variable introduced: **



*   x = Current period
1. Advance to the next row in system record of simulation pay stage for Period x +1.
2. Copy all values from previous row.
3. Assign SyRec11 the value of SyRec10.
4. Assign SyRec13 the value of SyRec12.
5. Assign SyRec18 the value of SyRec17.
6. Assign SyRec10, SyRec12, and SyRec17 = 0.
7. Assign SyRec3, SyRec5, and SyRec6 = 0.
8. <span style="text-decoration:underline;">If</span> UsRec8 = Defected, Skipped, or Quit, <span style="text-decoration:underline;">then</span>:
    1. UsRec8 = NR
    2. UsRec3 = 0
    3. UsRec5 = NR
    4. UsRec12 = NR
9. Go to UsFunc

_Path 2_



1. Write the following to a log file:
    1. Log1 = EV1 = Z, where &lt;x> is the number of members at the start of the simulation
    2. Log2 = SyRec1 (final period) = Y, where &lt;x> is the number of valid members remaining at the end of the simulation
    3. 

<p id="gdcalert41" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert42">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 = &lt;x>% of policyholders that left the group by end of simulation
    4. Log4 = SyRec19 (Period 1) = B, where &lt;x> was the initial premium members were asked to pay
    5. Log5 = SyRec19 (final period) = A, where &lt;x> is the final premium members were asked to pay
    6. 

<p id="gdcalert42" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert43">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 = &lt;x>% increase of premiums by the end of the simulation
    7. Log7 = SyRec3 (Period 0 Finalize) = C
    8. Log8 = EV4 = &lt;x>% of policyholders who were assigned to Defect
    9. 

<p id="gdcalert43" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert44">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 = &lt;x>% of policyholders who actually defected
    10. Log10 = PV5 = &lt;x>% of the initial collapse threshold set for PV5
2. For single runs, store the table of system record as a .csv file.

See the additional specification for automating the simulation and performing cumulative runs testing the collapse threshold:

[insert specification for multiple simulation runs here]





12. What the protocol <span style="text-decoration:underline;">might</span> do one day

Questions the simulation might be able to answer are as follows:



1. Chart the cumulative number of defections over the course of the simulation. At termination, did the community collapse?
    1. Iterative runs = the boundary condition for system input variables that produce community collapse.
2. What percentage of honest participants are required to produce groups which collapse?
3. How do the different variable inputs contribute to changing the collapse threshold? 
    2. Collapse is x% likely to occur with x% of initial defectors = modifying all other variables
