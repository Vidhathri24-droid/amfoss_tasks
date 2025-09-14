# The CommandLine Cup

----------------------

### Part-1:Enter the maze

I started doing the task by cloning the github repository using the below command.

```
https://github.com/KshitijThareja/TheCommandLineCup.git
```

Then I created a folder named codes on my machine and organized all the tasks related to Amfoss into a main folder called Amfoss-Tasks.

------------------------

### Part-2: First Challenge

While reading the task to find the first spell, I figured out that the first perfect number is 6, so the code is located in the directory named 06 and when differentiating the equation (x^2 - 7x) w.r.t x we get the value of y as 2x-7. So we get the value of y as 5. So, the spell is stored in the Spell_07.txt in the directory 06. When I opened the file, I got to know that the spell is 'Impedimenta'. So next, I navigated to the spellbook directory and executed the python file 'Impedimenta.py' using python3. I got the secret code and then I stored it in a file named Part_02.txt in the codes folder.


-----------------------------

### Part-3: Second Challenge

In part-3, I figured out that the first element used to make the semiconductors is Germanium(Ge). It's atomic number is 32. So, the next spell is stored in Spell_03.txt file of 02 directory. When I opened it, I got to know the spell i.e., Stupefy.

Then I navigated to the spellbook directory and executed the Stupefy file using Python3 and when I executed it, I got an other secret code. Then I stored it in the Part_03.txt file in the codes directory.

----------------------------

### Part-4: Third Challenge

In part-4, I got to know the subject that is taught by the Professor Lupin at Hogwarts (defenseAgainstTheDarkArts). The shape-shifting creature is the 'Boggart". The spell used to fight with the boggart is "Riddikulus". There is a python file "Riddiculus.py" in the spellbook directory in the "defenseAgainstTheDarkArts) branch.

To switch the branch I used the command ```git checkout defenseAgainstTheDarkArts```. Then I executed the following command from the main branch by cd'ing into the required folder ```git checkout <remote branch> -- <Relative path of the file to be copied from the other branch>```. After this the Riddiculus.py can be executed from the main branch. The secret code obtained by executing the python file is  stored in a file named Part_04.txt in the codes directory.

----------------------------

### Part-5: Fourth Challenge

As the spell for this task is hidden in the commit logs of the repository we can use ```git logs``` to see the logs.

There is a hint saying that "Hey there! The last spell is in path 0x/Spell_0y" of thegraveyard...
    where x is the number of horcruxes made by Voldemort and y is the number that has same alphabets as the number"
    
    The number of horcruxes made by Voldemort is 7. 
    The number that has the same number of alphabets is 4.
    So the spell is stored in the Spell_04 file of 07 directory of the 'thegraveyard' branch.
    
The spell stored in Spell_04 file of 06 directory of the 'thegraveyard' branch is 'Priori  Incantatem' when I run this python file, I was able to get the final part of the spell and I stored it in the Part_05.txt in the codes directory of the main branch.

Then I concatenated all the parts of the spells into a single file named Encoded.txt.

Then I decoded this in base64 using the below command

```
cat Encoded.txt | base64 --decode
```
----------------------------------








