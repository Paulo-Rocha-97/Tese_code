# This function connects all the models to be evaluated connected

from os import path
from tensorflow import keras
#%% Call all models

Name_model_1 = 'Example'
Name_model_2 = 'Example'
Name_model_3 = 'Example'
Name_model_4 = 'Example'

def load_models(Name_model_1,Name_model_2,Name_model_3, Name_model_4):

    folder = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code'
    
    Verify =  int(path.exists(folder+'/Model_1/Results/'+Name_model_1)) + \
              int(path.exists(folder+'/Model_2/Results/'+Name_model_2)) + \
              int(path.exists(folder+'/Model_3/Results/'+Name_model_3)) + \
              int(path.exists(folder+'/Model_4/Results/'+Name_model_4))
    
    if Verify == 4:
        
        # load json and create model
        
        json_file = open(folder+'/Model_1/Results/'+Name_model_1+'/model1_'+Name_model_1+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_1 = keras.models.model_from_json(loaded_model_json)
        json_file = open(folder+'/Model_2/Results/'+Name_model_2+'/model2_'+Name_model_2+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_2 = keras.models.model_from_json(loaded_model_json)
        json_file = open(folder+'/Model_2/Results/'+Name_model_2+'/model2_sec_'+Name_model_2+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_2_sec = keras.models.model_from_json(loaded_model_json)
        json_file = open(folder+'/Model_3/Results/'+Name_model_3+'/model3_'+Name_model_3+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_3 = keras.models.model_from_json(loaded_model_json)
        json_file = open(folder+'/Model_3/Results/'+Name_model_3+'/model3_sec_'+Name_model_3+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_3_sec = keras.models.model_from_json(loaded_model_json)
        json_file = open(folder+'/Model_4/Results/'+Name_model_4+'/model4_'+Name_model_4+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_4 = keras.models.model_from_json(loaded_model_json)
        json_file = open(folder+'/Model_4/Results/'+Name_model_4+'/model4_sec_'+Name_model_4+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model_4_sec = keras.models.model_from_json(loaded_model_json)
        
        # load weights into new model
        
        model_1.load_weights(folder+'/Model_1/Results/'+Name_model_1+'/model1_'+Name_model_1+'.h5')    
        model_2.load_weights(folder+'/Model_2/Results/'+Name_model_2+'/model2_'+Name_model_2+'.h5')
        model_2_sec.load_weights(folder+'/Model_2/Results/'+Name_model_2+'/model2_sec_'+Name_model_2+'.h5')
        model_3.load_weights(folder+'/Model_3/Results/'+Name_model_3+'/model3_'+Name_model_3+'.h5')
        model_3_sec.load_weights(folder+'/Model_3/Results/'+Name_model_3+'/model3_sec_'+Name_model_3+'.h5')
        model_4.load_weights(folder+'/Model_4/Results/'+Name_model_4+'/model4_'+Name_model_4+'.h5')
        model_4_sec.load_weights(folder+'/Model_4/Results/'+Name_model_4+'/model4_sec_'+Name_model_4+'.h5')
        
        
    
    else:
        
        print('\n------------------------------------\nAn error occurred please check the name of the models and the path\n------------------------------------')