#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyopenms')


# In[2]:


import pyopenms


# In[6]:


print ("Avogadro's number is",pyopenms.Constants.AVOGADRO)


# In[7]:


from pyopenms import*


# In[8]:


edb=ElementDB()


# In[9]:


edb.hasElement("O")


# In[14]:


oxygen=edb.getElement("O")


# In[16]:


print(oxygen.getName( ))


# In[17]:


print(oxygen.getSymbol())


# In[18]:


print(oxygen.getMonoWeight())


# In[19]:


print(oxygen.getAverageWeight())


# In[23]:


print("One mole of oxygen weighs" ,2*oxygen.getAverageWeight(),"grams")


# In[24]:


sulfur=edb.getElement("S")
print(sulfur.getName( ))
print(sulfur.getSymbol())
print(sulfur.getMonoWeight())
print(sulfur.getAverageWeight())


# In[27]:


isotopes=sulfur.getIsotopeDistribution()


# In[28]:


print ("One mole of 16O2 weighs", 2*oxygen.getMonoWeight(), "grams")


# In[29]:


edb = ElementDB()
oxygen_isoDist = {"mass": [], "abundance": []}
oxygen = edb.getElement("O")
isotopes = oxygen.getIsotopeDistribution()
for iso in isotopes.getContainer():
    print ("Oxygen isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")
    oxygen_isoDist["mass"].append(iso.getMZ())
    oxygen_isoDist["abundance"].append((iso.getIntensity() * 100))


# In[30]:


edb = ElementDB()


isotopes = edb.getElement("C").getIsotopeDistribution().getContainer()


carbon_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()


# In[31]:


print ("Mass difference between 12C and 13C:", carbon_isotope_difference)


# In[32]:


isotopes=edb.getElement("N").getIsotopeDistribution().getContainer()
Nitrogen_isotope_difference=isotopes[1].getMZ()-isotopes[0].getMZ()
print ("Mass difference between 14N and N15:",Nitrogen_isotope_difference)


# In[34]:


print ("Relative deviation:", 100*(carbon_isotope_difference -Nitrogen_isotope_difference)/carbon_isotope_difference, "%")


# In[35]:


lys=ResidueDB().getResidue("Lysine")


# In[36]:


print(lys.getName())


# In[37]:


print(lys.getThreeLetterCode())


# In[38]:


print(lys.getOneLetterCode())


# In[40]:


print(lys.getAverageWeight())


# In[42]:


print(lys.getMonoWeight())


# In[43]:


print(lys.getPka())


# In[44]:


print(lys.getFormula().toString())


# In[45]:


uridine = RibonucleotideDB().getRibonucleotide(b"U")


# In[46]:


print(uridine.getName())
print(uridine.getCode())
print(uridine.getAvgMass())
print(uridine.getMonoMass())
print(uridine.getFormula().toString())
print(uridine.isModified())
methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")
print(methyladenosine.getName())
print(methyladenosine.isModified())


# In[ ]:




