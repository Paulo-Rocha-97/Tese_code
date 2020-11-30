function [U,Y] = Correct_data_format_m1()

load('model_1_data.mat');
Comp = size(u);
U=zeros(Comp(1),Comp(2));
Y=zeros(Comp(1),1);
NaN_val_u = isnan(u);
NaN_val_y = isnan(y');
for i = 1:Comp(1)
    for j = 1:Comp(2)
        if NaN_val_u(i,j)==1
            if i == 1
                U(i,j) = 91.3;
            else
                U(i,j) = U((i-1),j);
            end
        else
            U(i,j) = u(i,j);
        end
    end
    if NaN_val_y(i)==1
        Y(i) = Y(i-1);
    else
        Y(i) = y(1,i);
    end
end
end

