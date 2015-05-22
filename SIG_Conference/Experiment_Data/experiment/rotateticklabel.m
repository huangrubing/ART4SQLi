function th=rotateticklabel(h,rot)
%ROTATETICKLABEL rotates tick labels
% TH=ROTATETICKLABEL(H,ROT) ris the calling form where H is a handle to
% the axis that contains the XTickLabels that are to be rotated. ROT is
% an optional parameter that specifies the angle of rotation. The default
% angle is 90. TH is a handle to the text objects created. For long
% strings such as those produced by datetick, you may have to adjust the
% position of the axes so the labels don't get cut off.
%
% Of course, GCA can be substituted for H if desired.
%
% TH=ROTATETICKLABEL([],[],'demo') shows a demo figure.
%
% Known deficiencies: if tick labels are raised to a power, the power
% will be lost after rotation.
%
% See also datetick.
% Written Oct 14, 2005 by Andy Bliss
% Copyright 2005 by Andy Bliss
if nargin==3
x=[now-.7 now-.3 now];
y=[20 35 15];
figure
plot(x,y,'.-')
datetick('x',0,'keepticks')
h=gca;
set(h,'position',[0.13 0.35 0.775 0.55])
rot=90;
end
%set the default rotation if user doesn't specify
if nargin==1
rot=45;
end
%make sure the rotation is in the range 0:360 (brute force method)
% while rot>360
% rot=rot-360;
% end
% while rot<0
% rot=rot+360;
% end
%get current tick labels
a=get(h,'XTickLabel');
%erase current tick labels from figure
set(h,'XTickLabel',[]);
%get tick label positions
b=get(h,'XTick');
c=get(h,'YTick');
%make new tick labels
if rot<180
th=text(b,repmat(c(1)-.1*(c(2)-c(1)),length(b),1),a,'HorizontalAlignment','right','fontsize',10,'fontweight','normal','rotation',rot);
set(h,'xticklabel','');% 将原有的标签隐去
else
th=text(b,repmat(c(1)-.1*(c(2)-c(1)),length(b),1),a,'HorizontalAlignment','left','fontsize',10,'fontweight','normal','rotation',rot);
set(h,'xticklabel','');% 将原有的标签隐去
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%r> 使用方法：
% y3=[24.2 15.3 26.51 38.53 25.98 31.94 25.31 29.85];
% x1=[1 2 3 4 5 6 7 8];
% bar(x1,y3,'k');
% set(gca,'xticklabel',{'CON','OA','AFMK','AFMK+OA','Mel','Mel+OA','VitE','VitE+OA'});
% h=gca;
% th=rotateticklabel(h,-30);