function result_boxplot(result,result_title,x_title,y_title)
%根据输入的实验数据result生成boxplot
%result 列作为一组数据，计算相应的boxplot
%result 行作为不同组别的实验数据
%方形图
%title根据输入参数result_title确定
%xlabel根据输入参数x_title确定
%ylabel根据输入参数y_title确定
result=result';
boxplot(result);
axis square;
title(result_title);
% xlabel(x_title);
ylabel(y_title);
%figure 画另一幅图
%hold on 保持当前画布 继续在当前画布画图
%%%%%%%%%%%%%%%%%  设置坐标标签  %%%%%%%%%%%%%%%%%%%%
% axis([0.5 9.5 200 2200])%设置x y坐标范围
% set(gca,'XTick',1:9)
% set(gca,'XTickLabel',{'project.php','status.php','resolution.php','severity.php','priority.php','os.php','database.php','site.php','bug.php'})
% h=gca;
% rotateticklabel(h)
% set(gca,'XTick',[])
% set(gca,'XTickLabel',{'project.php','status.php','resolution.php','severity.php','priority.php','os.php','database.php','site.php','bug.php'})
