function [] = plot_vectors(my_vector,line_spec,line_width,leg_name,my_vector2,line_spec2,line_width2,leg_name2)
    theta = linspace(0, 2*pi, 360);
    
    my_plot0 = plot(cos(theta), sin(theta), 'k','DisplayName','unit circle'); hold on;
    my_plot1 = plot([0 my_vector(1,1)],[0 my_vector(1,2)], line_spec,'MarkerSize',12, ...
        'LineWidth',line_width,'DisplayName',leg_name); hold on;
    my_plot2 = plot([0 my_vector2(1,1)],[0 my_vector2(1,2)], line_spec2,'MarkerSize',12, ...
        'LineWidth',line_width2,'DisplayName',leg_name2); hold on;
    
    for i=2:length(my_vector(:,1))
        hold on;
        plot([0 my_vector(i,1)],[0 my_vector(i,2)], line_spec,'MarkerSize',12,'LineWidth',line_width);
    end
    hold on;
    for i=2:length(my_vector2(:,1))
        hold on;
        plot([0 my_vector2(i,1)],[0 my_vector2(i,2)], line_spec2,'MarkerSize',12,'LineWidth',line_width2);
    end
    hold off;
    legend([my_plot0 my_plot1 my_plot2],'Location','southeast');
end