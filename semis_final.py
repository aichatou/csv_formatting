import sys
import csv
from collections import OrderedDict 

###################### fonction qui retourne l'index d'une variable #########################################################
def if_test(header, var):
   if var in header:
      return (header.index(var))
      
###################### function semis1() ####################################################################################
      
def semis1(): # function qui construit un fichier type reproduction 
 repr = []
 csvinput= open(sys.argv[1],'r')
 h0 = csv.reader(csvinput, delimiter = '\t').next() 
 h = ['project','sown_year','harvested_year','id_seed_lot_sown','intra_selection_name','etiquette','split','quantity_sown','quantity_harvested','block','X','Y']
 [h.append(x) for x in h0]
 for row in csv.reader(csvinput, delimiter = '\t'):

       if row[if_test(h0,'type')] != 'Melange': # tester si le type (de la variété) n'est pas un mélange
        if row[if_test(h0,'variete')]!="" and row[if_test(h0,'agriculteur')]!= "": #tester si les variables 'variété' et 'agriculteur' ne sont pas vides     
         row0 = row[if_test(h0,'variete')] + "_"  + row[if_test(h0,'agriculteur')][0:3] + "_" + sys.argv[3] #costruire le lot de graine
         row1 = sys.argv[2] # nom du projet
         row2 = sys.argv[3] # l'année 
         row3 = sys.argv[4] #la variété
         val = [row1,row2,row3,row0,'','',0,'','',1,'','']
         for term in row:
          val.append(term)
         repr.append(val)
 csvinput.close()
 return repr
         

######################## function inn1() #######################################################################################
def inn1(): # function qui calcule et remplace les lignes dupliquées du fichier INN par leur moyenne 

 inn_lign = OrderedDict() #
 inn_lines = []
 innn = OrderedDict() #
 inn = []

 csvinput2= open(sys.argv[5],'r')
 hd1 = csv.reader(csvinput2, delimiter = '\t').next()
 for row in csv.reader(csvinput2, delimiter = '\t'):  
  inn_lines.append(row) 

 i=0
 prec = ['' for x in range(6)]
 
 for val2 in inn_lines:
      inn_line = val2

      if (inn_line[if_test(hd1, 'ecartement')] != 'NA'):
	  # convertir les valeurs de string à  float
       inn_line[if_test(hd1, 'ecartement')] = float(inn_line[if_test(hd1, 'ecartement')].replace(',', '.'))
      if (inn_line[if_test(hd1, 'poids_frais')] != 'NA'):# or (inn_line[5] != 'NA') or (inn_line[6] != 'NA'):
       inn_line[if_test(hd1, 'poids_frais')] = float(inn_line[if_test(hd1, 'poids_frais')].replace(',', '.'))
      if (inn_line[if_test(hd1, 'poids_sec')] != 'NA'):# or (inn_line[5] != 'NA') or (inn_line[6] != 'NA'):
       inn_line[if_test(hd1, 'poids_sec')] = float(inn_line[if_test(hd1, 'poids_sec')].replace(',', '.'))
      if (inn_line[if_test(hd1, 'mat_seche')] != 'NA'):
       inn_line[if_test(hd1, 'mat_seche')] = float(inn_line[if_test(hd1, 'mat_seche')].replace(',', '.'))
	   # tester pour les variables variété et agriculteur si la valeur courante = la valeur précedente 
      if (prec[0] == inn_line[if_test(hd1, 'agriculteur')] and prec[1] == inn_line[if_test(hd1, 'variete')]):
	  # si test = oui, attribuer à la valeur courante, la moyenne de la courante et de la précédente
         inn_line[if_test(hd1, 'ecartement')] = (inn_line[if_test(hd1, 'ecartement')] + prec[2])/2
         inn_line[if_test(hd1, 'poids_frais')] = (inn_line[if_test(hd1, 'poids_frais')]+ prec[3])/2
         inn_line[if_test(hd1, 'poids_sec')] = (inn_line[if_test(hd1, 'poids_sec')] + prec[4])/2
         inn_line[if_test(hd1, 'mat_seche')] = (inn_line[if_test(hd1, 'mat_seche')] + prec[5])/2
      # Récupérer à chaque étape, la valeur précédente de la variable
      prec[0] = inn_line[if_test(hd1, 'agriculteur')] ]
      prec[1] = inn_line[if_test(hd1, 'variete')]
      prec[2] = inn_line[if_test(hd1, 'ecartement')]
      prec[3] = inn_line[if_test(hd1, 'poids_frais')] 
      prec[4] = inn_line[if_test(hd1, 'poids_sec')] 
      prec[5] = inn_line[if_test(hd1, 'mat_seche')] 
      #convertir les valeurs de float à string
      inn_line[if_test(hd1, 'ecartement')] = str(inn_line[if_test(hd1, 'ecartement')])
      inn_line[if_test(hd1, 'poids_frais')] = str(inn_line[if_test(hd1, 'poids_frais')])
      inn_line[if_test(hd1, 'poids_sec')] = str(inn_line[if_test(hd1, 'poids_sec')])
      inn_line[if_test(hd1, 'mat_seche')] = str(inn_line[if_test(hd1, 'mat_seche')])

	  # récupération des lignes en éliminant les duplicats
 str_vals = []
 newrows = []
 for val in inn_lines:
    vlue = [val[if_test(hd1, 'agriculteur')], val[if_test(hd1, 'variete')]]
    str_val = ';'.join(vlue) #convertir liste vlue en chaine de caractère
    str_vals.append(str_val) # ajouter la chaine à la liste 'str_vals'
    if vlue not in newrows: # tester si la chaine n'existe pas déjà dans la liste
        newrows.append(vlue)# si oui, l ajouter à la liste
        
 unique_vals = {val: i for i, val in enumerate(str_vals)} #les dernieres occurences de chaque valeur

 # chercher l'indice de chaque occurence et récupérer sa valeur
 i=0
 for val in inn_lines:
  if (i==unique_vals[';'.join([val[if_test(hd1, 'agriculteur')], val[if_test(hd1, 'variete')]])]):
   inn.append(val)
  i+=1 
 return inn



######################## function inn2() #######################################################################################
def inn2(): #function qui ajoute toutes  les variables du fichier inn2 au fichier de reproduction semis1 en fonction du nom de la variété et de celui de l'agriculteur

 semis1_inn =[]

 i=0
 prec1 = ''
 prec2 = ''

 for val in semis1(): 
  p = ['' for x in range(4)]
  rep_line = val

  for val2 in inn1():
   inn_line = val2
   if (rep_line[12] == inn_line[0]) and (rep_line[14] == inn_line[2].upper()): #tester l'égalité du nom de la variété et de celui de l'agriculteur dans les deux fichiers
      if (prec1 == inn_line[0] and prec2 == inn_line[2]):
         writer.writerow(rep_line)
         rep_line = rep_line[0:len(rep_line)-4]
         val0 = inn_line[3:7] #les 4  variables inn à ajouter 
         [rep_line.append(x) for x in val0] #ajout des variables au fichier reproduction
         rep_line = rep_line[0:len(rep_line)-4]###

      prec1 = inn_line[0]
      prec2 = inn_line[2]
      val1 = inn_line[3:7]
      #print val1
      [rep_line.append(x) for x in val1]
      i+=1

  if len(rep_line) == 44 :
   [rep_line.append(x) for x in p]
  semis1_inn.append(rep_line)
 return semis1_inn
  
  
######################## function rsh1() #######################################################################################
def rsh1(): #

 agric = []
 for v in semis1():
   agric.append(v[12])
 agric_sans_doublons = list(set(agric))


 csvinput3= open(sys.argv[6],'r')
 header3 = csv.reader(csvinput3,delimiter = '\t').next()

 ag = []
 for row in csv.reader(csvinput3,delimiter = '\t'):
     ag.append(row[if_test(header3,'agriculteur')]) 
 csvinput3.close()

 unique_vals1 = {val: i for i, val in reversed(list(enumerate(ag)))}
 unique_vals = {val: i for i, val in enumerate(ag)}

############################################################ ##########################################################################


 rsh = []
 p = ['' for x in range(42)]
 csvinput3= open(sys.argv[6],'r')
 header3 = csv.reader(csvinput3,delimiter = '\t').next()
 i=0

 for row in csv.reader(csvinput3,delimiter = '\t'): #pour chaque ligne du fichier rsh
     if row[if_test(header3,'agriculteur')] in agric_sans_doublons: "tester l existence du nom de l agriculteur"
       if i ==unique_vals1[row[if_test(header3,'agriculteur')]]:
         p = ['' for x in range(42)]

       p[0] = row[if_test(header3,'agriculteur')]
       if row[if_test(header3,'horizon')] == '0-30': 
         # récupérer toutes les valeurs à horizon = '0-30'
         p[1:15] = [row[if_test(header3,'poids_hum_rsh')],row[if_test(header3,'poids_sec_rsh')], row[if_test(header3,'humidite_rsh')],row[if_test(header3,'NO3_bloc')],row[if_test(header3,'NH4_bloc')],row[if_test(header3,'NO3_horiz')],row[if_test(header3,'NH4_horiz')],row[if_test(header3,'N_tot_horiz')],row[if_test(header3,'prop_N_tot')],row[if_test(header3,'NO3_tot')],row[if_test(header3,'prop_NO3_tot')],row[if_test(header3,'NH4_tot')],row[if_test(header3,'prop_NH4_tot')],row[if_test(header3,'N_tot')] ]
         

       if row[if_test(header3,'horizon')] == '30-60': 
	   # récupérer toutes les valeurs à horizon = '30-60'
         p[15:29] = [row[if_test(header3,'poids_hum_rsh')],row[if_test(header3,'poids_sec_rsh')], row[if_test(header3,'humidite_rsh')],row[if_test(header3,'NO3_bloc')],row[if_test(header3,'NH4_bloc')],row[if_test   (header3,'NO3_horiz')],row[if_test(header3,'NH4_horiz')],row[if_test(header3,'N_tot_horiz')],row[if_test(header3,'prop_N_tot')],row[if_test(header3,'NO3_tot')],row[if_test(header3,'prop_NO3_tot')],row[if_test(header3,'NH4_tot')],row[if_test(header3,'prop_NH4_tot')],row[if_test(header3,'N_tot')] ]

       if row[if_test(header3,'horizon')] == '60-90': 
	   # récupérer toutes les valeurs à horizon = '60-90'
         p[29:43] = [row[if_test(header3,'poids_hum_rsh')],row[if_test(header3,'poids_sec_rsh')], row[if_test(header3,'humidite_rsh')],row[if_test(header3,'NO3_bloc')],row[if_test(header3,'NH4_bloc')],row[if_test(header3,'NO3_horiz')],row[if_test(header3,'NH4_horiz')],row[if_test(header3,'N_tot_horiz')],row[if_test(header3,'prop_N_tot')],row[if_test(header3,'NO3_tot')],row[if_test(header3,'prop_NO3_tot')],row[if_test(header3,'NH4_tot')],row[if_test(header3,'prop_NH4_tot')],row[if_test(header3,'N_tot')] ]
  

       if i ==unique_vals[row[if_test(header3,'agriculteur')]]:
         rsh.append(p)
     i+=1
 return rsh
 
 
######################## function rsh2() #######################################################################################
def rsh2(): #function qui ajoute toutes  les variables du fichier rsh au fichier de reproduction semis1 en fonction du nom de l'agriculteur

 semis1_rsh = []
 k=0
 for data in inn2():
  for line in rsh1():
   if data[12] == line[0]: # identifier les lignes où l'agriculteur est le même dans inn2 et rsh1
      k+=1
      [data.append(x) for x in line[1:len(line)]]
  semis1_rsh.append(data)
 return semis1_rsh
 
 
######################## function semis_final() #######################################################################################
def semis_final(): #ajouter les variables du fichier itk au fichier de reproduction en fonction du nom de l agriculteur

 semis = []
 csvinput4= open(sys.argv[7],'r')
 hd4 = csv.reader(csvinput4,delimiter = '\t').next()
 if 'agriculteur' in hd4:
  index_var_agriculteur4 = hd4.index( 'agriculteur' )

 itk_lines = []
 for row in csv.reader(csvinput4,delimiter = '\t'):  
  itk_lines.append(row)
 csvinput4.close()

 csvinput4= open(sys.argv[7],'r')
 header4 = csv.reader(csvinput4,delimiter = '\t').next()


 for data in rsh2():
  for line in itk_lines:
   if data[12] == line[0]: # identifier les lignes où l'agriculteur est le même dans rsh2 et itkd
      [data.append(x) for x in line[2:len(line)]]
  #writer.writerow(data)
  semis.append(data)
 return semis
  
 
 
  
 ########################################### main ########################################################################################################

def main():

 csvinput= open(sys.argv[1],'r')
 h0 = csv.reader(csvinput, delimiter = '\t').next() 
 #ajouter les en tetes des fichiers inn, rsh, itk au fichier semis (reproduction)
 h = ['project','sown_year','harvested_year','id_seed_lot_sown','intra_selection_name','etiquette','split','quantity_sown','quantity_harvested','block','X','Y']
 
 h_inn2 = ['ecartement', 'poids_frais','poids_sec','mat_seche']
  
 
 h_rsh = [
'0_30_poids_hum_rsh', '0_30_poids_sec_rsh','0_30_humidite_rsh', '0_30_NO3_bloc','0_30_NH4_bloc','0_30_NO3_horiz', '0_30_NH4_horiz','0_30_N_tot_horiz', '0_30_prop_N_tot','0_30_NO3_tot','0_30_prop_NO3_tot', '0_30_NH4_tot','0_30_prop_NH4_tot','0_30_N_tot', '30_60_poids_hum_rsh','30_60_poids_sec_rsh','30_60_humidite_rsh','30_60_NO3_bloc','30_60_NH4_bloc','30_60_NO3_horiz','30_60_NH4_horiz','30_60_N_tot_horiz','30_60_prop_N_tot','30_60_NO3_tot','30_60_prop_NO3_tot',
'30_60_NH4_tot','30_60_prop_NH4_tot','30_60_N_tot',
'60_90_poids_hum_rsh','60_90_poids_sec_rsh','60_90_humidite_rsh','60_90_NO3_bloc','60_90_NH4_bloc','60_90_NO3_horiz','60_90_NH4_horiz','60_90_N_tot_horiz','60_90_prop_N_tot','60_90_NO3_tot','60_90_prop_NO3_tot','60_90_NH4_tot',
'60_90_prop_NH4_tot','60_90_N_tot']

 
 h_itk = ['type_sol','precedent','travail_sol','densite_semis','N1','date_N1','N2','date_N2','N3','date_N3','N4','date_N4',
'autre_ferti','quanti_autre_ferti','date_autre_ferti','Herbi1','date_Herbi1','Herbi2','date_Herbi2','Herbi3','date_Herbi3',
'Fongi_1','date_Fongi1','Fongi_2','date_Fongi2','Fongi_3','date_Fongi3','Insecti1','date_Insecti1','Insecti2',	'date_Insecti2','Insecti3',
'date_Insecti3'	,'Regul','date_Regul' ]

 [h.append(x) for x in (h0 + h_inn2 + h_rsh+ h_itk)]
 
 writer = csv.writer(open(sys.argv[8], 'w'),delimiter = '\t')
 writer.writerow(h)
 for row in semis_final():
   writer.writerow(row)



############################################################ #####################################################################################################################################################################

#python semis_final.py SYNTH_MOY2_2015.csv wheatamix 2014 2015 INN_2015.csv  RSH_2015.csv ITK_2015.csv final6.csv

 
if __name__ == '__main__':
  if len(sys.argv) == 9:
    main()   
  else:
    print('Nombre d"arguments systeme incorrect')


           
