% Kohonen network

clc; clear; close all;

% Initial values
x = [-1 0; 0 1; 1/sqrt(2) 1/sqrt(2)]; % input
w = [-1 0; -2/sqrt(5) 1/sqrt(5); -1/sqrt(5) 2/sqrt(5)] % weights
lr = 0.5;   % learning rate

% x = [1 1 0 0; 0 0 0 1; 1 0 0 0; 0 0 1 1];
% w = [0.2 0.6 0.5 0.9; 0.8 0.4 0.7 0.3]
% lr = 0.6;
%% a) Plot unit circle diagram
starts = zeros(3,2);

%plot data and weights
figure();
plot_vectors(x,'--m*',1.7,'data',w,'-bo',0.7,'weights'); 
title('data and *initial* weigths'); grid on;
xlabel('dimension 1'); ylabel('dimension 2');

%% b) Net training

% % Normalization
% x = x./norm(x)
% w = w./norm(w)

for epoch=1:2
    % Distances
    d = zeros(length(x(:,1)), length(w(:,1)));
    for i=1:length(x(:,1))
        for j=1:length(w(:,1))
            d(i,j) = norm(x(i,:)-w(j,:));
        end
    end
    % Update Weights
    [min_d,min_ind] = min(d,[],2)
    for i=1:length(x')
        w(min_ind(i),:) = w(min_ind(i),:) + lr*(x(i,:)-w(min_ind(i),:) );
    end
    
    %plot nmd data
    figure();
    plot_vectors(x,'--m*',1.7,'data',w,'-bo',0.7,'weights'); 
    my_title = sprintf('data and *intermediate%d* weigths',epoch);
    title(my_title); grid on;
    xlabel('dimension 1'); ylabel('dimension 2');
    
    disp("epoch finished. Here are the new weights:")
    disp("(Rows: weights, Col: dims)")
    disp(w)
end

%plot nmd data
figure();
plot_vectors(x,'--m*',1.7,'data',w,'-bo',0.7,'weights'); 
title('data and *trained* weigths'); grid on;
xlabel('dimension 1'); ylabel('dimension 2');
