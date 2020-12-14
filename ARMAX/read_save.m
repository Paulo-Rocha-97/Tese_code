function [Data] = read_save(Val_data,Model,filename,data_name)

%Val_data = Val_data(:,[],:);

[ypred] = sim(Model,Val_data);

Y_pred =  get( ypred, 'outputData' );

load(data_name);

Y=y(1159:end,:);

Data = [Y,Y_pred];

writematrix(Data,filename) 
end

