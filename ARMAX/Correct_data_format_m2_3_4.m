function [U,Y,U_sec,Y_sec] = Correct_data_format_m2_3_4(file_name)

load(file_name);
Comp = size(u);
U=zeros(Comp(1),Comp(2));
Y=zeros(Comp(1),1);
NaN_val_u = isnan(u);
NaN_val_y = isnan(y');
for i = 1:Comp(1)
    for j = 1:Comp(2)
        if NaN_val_u(i,j)==1
            if i == 1
                fprintf('Index 1 error - U')
            else
                U(i,j) = U((i-1),j);
            end
        else
            U(i,j) = u(i,j);
        end
    end
    if NaN_val_y(i)==1
        if i ==1
            fprintf('Index 1 error - Y')
        else
            Y(i) = Y(i-1);
        end
    else
        Y(i) = y(i);
    end
end
Comp = size(u_sec);
U_sec=zeros(Comp(1),Comp(2));
Y_sec=zeros(Comp(1),1);
NaN_val_u_sec = isnan(u_sec);
NaN_val_y_sec = isnan(y_sec');
for i = 1:Comp(1)
    for j = 1:Comp(2)
        if NaN_val_u_sec(i,j)==1
            if i == 1
                fprintf('index 1 error - U_sec')
            else
                U_sec(i,j) = U_sec((i-1),j);
            end
        else
            U_sec(i,j) = u_sec(i,j);
        end
    end
    if NaN_val_y_sec(i)==1
        if i == 1
            fprintf('index 1 error - Y_sec')
        else
            Y_sec(i) = Y_sec(i-1);
        end
    else
        Y_sec(i) = y_sec(i);
    end
end

end

