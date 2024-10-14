local scrName;

game:GetService("StarterGui"):SetCore("SendNotification", {Title = "Script",Text = "Loading, Please wait. Don't re-execute yet or if it take long time already then re-execute",Duration = 10})
game:GetService("StarterGui"):SetCore("SendNotification", {Title = "Script",Text = "After check key, sometimes you have to re-execute to make tthe script show",Duration = 10})

if game.GameId == 4367208330 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/refs/heads/main/PressureW.py';
elseif game.GameId == 1235188606 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/main/DragonAdventure.py';
elseif game.GameId == 2440500124 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/main/Door.py';
elseif game.GameId == 2294168059 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/refs/heads/main/TheMimic.py';
elseif game.GameId == 1000233041 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/refs/heads/main/SCP3008.py';
elseif game.GameId == 5569032992 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/refs/heads/main/DiddyWorld.py';
elseif game.GameId == 4367208330 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/refs/heads/main/PressureW.py';
elseif game.GameId == 5750914919 then
	scrName = 'https://raw.githubusercontent.com/Yumiara/Python/refs/heads/main/Fisch-XYZ.cpp';
end;


if scrName then
	local source = game:HttpGetAsync(scrName);
	local Env = loadstring(source);
	
	Env();
else
	game.Players.LocalPlayer:Kick('Unsupported Experience');
end;
