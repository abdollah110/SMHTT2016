import os
import ROOT
from ROOT import *
import array

rb_ = array.array("d",[0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000])

def MakeCompare(root1,hist1,root2,hist2,dataset ,lumi,Xaxis):
    
    ROOT.gStyle.SetFrameLineWidth(3)
    ROOT.gStyle.SetLineWidth(3)
    ROOT.gStyle.SetOptStat(0)
    
    c=ROOT.TCanvas("canvas","",0,0,600,600)
    c.cd()
    
    
    file1=TFile(root1,"open")
    print "---->,", file1.GetName()
    Histo1=file1.Get(hist1)
    Histo1.Scale(lumi/35.870)
#    Histo1=Histo1_.Rebin(len(rb_)-1,"",rb_)
    Histo1.SetLineColor(6)
    Histo1.SetLineWidth(2)
    Histo1.SetMaximum(Histo1.GetMaximum()*200)
    Histo1.SetMarkerColor(6)
    Histo1.SetMarkerStyle(24)
    
    file2=TFile(root2,"open")
    Histo2=file2.Get(hist2)
#    Histo2=Histo2_.Rebin(len(rb_)-1,"",rb_)
    Histo2.SetLineColor(9)
    Histo2.SetLineWidth(3)
    Histo2.SetMarkerColor(9)
    Histo2.SetMarkerStyle(20)
    
    

#    Histo1.SetTitle('')
    Histo1.GetXaxis().SetTitle('boson p_{T} (GeV)')
#    Histo1.GetXaxis().SetLabelSize(0.04)
#    Histo1.GetXaxis().SetNdivisions(505)
#    Histo1.GetXaxis().SetTitleSize(0.05)
#    Histo1.GetXaxis().SetTitleOffset(0.9)
#    Histo1.GetXaxis().SetLabelSize(0.04)
#    Histo1.GetXaxis().SetTitleFont(42)
#    Histo1.GetYaxis().SetTitle("Events")
#    Histo1.GetXaxis().SetRangeUser(50,1000)

    Histo1.GetXaxis().SetTitle("")
    Histo1.GetXaxis().SetTitleSize(0)
    Histo1.GetXaxis().SetLabelSize(0)
    Histo1.GetXaxis().SetNdivisions(505)
    Histo1.GetYaxis().SetLabelFont(42)
    Histo1.GetYaxis().SetLabelOffset(0.01)
    Histo1.GetYaxis().SetLabelSize(0.06)
    Histo1.GetYaxis().SetTitleSize(0.075)
    Histo1.GetYaxis().SetTitleOffset(1.04)
    Histo1.SetTitle("")
#    Histo1.Setlabel("")
    Histo1.GetYaxis().SetTitle("Events")
#    Histo1.GetXaxis().SetRangeUser(50,1000)    




    pad1 = ROOT.TPad("pad1","pad1",0,0.35,1,1)
    pad1.SetLogy()
    pad1.Draw()
    pad1.cd()
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetBorderSize(10)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.SetLeftMargin(0.18)
    pad1.SetRightMargin(0.05)
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.026)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameLineStyle(0)
    pad1.SetFrameLineWidth(3)
    pad1.SetFrameBorderMode(0)
    pad1.SetFrameBorderSize(10)
    
    
    
    
    
    
    Histo1.Draw()
    Histo2.Draw('same')
    
    
    categ  = ROOT.TPaveText(0.55, 0.5+0.013, 0.85, 0.5+0.1, "NDC")
    categ.SetBorderSize(   0 )
    categ.SetFillStyle(    0 )
    categ.SetTextAlign(   12 )
    categ.SetTextSize ( 0.06 )
    categ.SetTextColor(    1 )
    categ.AddText('Norm. ratio= %s'%str(format(Histo1.Integral()/Histo2.Integral(), '.2f')))
    categ.Draw()
    
    
    

    leg=ROOT.TLegend(0.4, 0.6, 0.95, 0.82, "", "brNDC")
    leg.SetLineWidth(1)
    leg.SetLineStyle(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.04)
#    leg.SetBorderSize(0)
    leg.SetTextFont(62)
    leg.AddEntry(Histo1,'DY#rightarrowll (ZTT)','lp')
    leg.AddEntry(Histo2,'Embedded %s (%s fb^{-1})'%(dataset,str(lumi)),'lp')
    leg.Draw()
    
    pad1.RedrawAxis()
    
    c.cd()
    pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.35);
    pad2.SetTopMargin(0.05);
    pad2.SetBottomMargin(0.35);
    pad2.SetLeftMargin(0.18);
    pad2.SetRightMargin(0.05);
    pad2.SetTickx(1)
    pad2.SetTicky(1)
    pad2.SetFrameLineWidth(3)
    pad2.SetGridx()
    pad2.SetGridy()
    pad2.Draw()
    pad2.cd()
    
    
    
    
    h1=Histo1.Clone()
    h1.SetMaximum(1.5)
    h1.SetMinimum(0.5)
    h1.SetMarkerStyle(24)
    h1.SetMarkerColor(6)
    h1.GetXaxis().SetTitle(Xaxis)
    
    
    
    h2=Histo2.Clone()
    
    
    h1.Sumw2()
    h2.Sumw2()
    
    
#    h3.Sumw2()

    h1.SetStats(0)
    h2.SetStats(0)
#    h3.SetStats(0)
    h1.SetTitle("")
    
    h1.Divide(h2)
#    h5.Divide(h2)

    
    h1.GetXaxis().SetTitle("")
    h1.GetXaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetTitle("DY / Embedded")
    h1.GetXaxis().SetNdivisions(505)
    h1.GetYaxis().SetNdivisions(5)
    h1.GetXaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleSize(0.1)
    h1.GetYaxis().SetTitleOffset(0.56)
    h1.GetXaxis().SetTitleOffset(1.04)
    h1.GetXaxis().SetLabelSize(0.11)
    h1.GetYaxis().SetLabelSize(0.11)
    h1.GetXaxis().SetTitleFont(42)
    h1.GetYaxis().SetTitleFont(42)
    h1.GetXaxis().SetTitle(Xaxis)
    
    h1.Draw()
#    h5.Draw("same")

    c.cd()
    pad1.Draw()
    
    ROOT.gPad.RedrawAxis()
    
    c.Modified()
    
    
    
    c.SaveAs('_Embed_%s%s.pdf'%(dataset,hist1))







##process=['TT','W','SingleTop','VV','ZTT','Codex_1200']
#process=['TT','W','SingleTop','VV','ZTT','Codex_14']
#Unc=['jes','jer','met_UES','met_JES']
#
#
#Input='_mj_LQMass_MT500_MET100_Iso.root'
##dir='Codex__mj_1_13TeV'
#dir='MuJet'
#
#for pro in process:
#    for unc in Unc:

plotInputEmbed=[
        ['embed_B.root','2016B',4.7],
        ['embed_C.root','2016C',2.2],
        ['embed_D.root','2016D',3.4],
        ['embed_E.root','2016E',3.8],
        ['embed_F.root','2016F',2.9],
        ['embed_G.root','2016G',7.4],
        ['embed_H.root','2016H',8.8],
        ['Tot_Embed.root','2016B-H',33.3],

        ]




FileNamesInfo=[
               
              ["Lep_pt_0jet","lep p_{T}","",5,1],
              ["Lep_eta_0jet","lep #eta","",10,1],
               
               ["Tau_pt_0jet","#tau p_{T} Lep (GeV)","",5,1],
               ["Tau_eta_0jet","#tau #eta","",10,1],
               
               ["Higgs_visMass_0jet","m_{vis} (GeV)","",5,1],
               ["Higgs_pt_0jet","Higgs p_{T} (GeV)","",10,1],
               
               ["mjj","m_{jj} (GeV)","",5,1],
               ["jpt_1","jet_{1} p_{T} (GeV)","",5,1],
               ["jpt_2","jet_{2} p_{T} (GeV)","",5,1],
               
               ["mt","m_{T} (GeV)","",5,1],
               ]


input='OUTPUTFiles/'



for i in range(0,len(FileNamesInfo)):
    for j in range(0,len(plotInputEmbed)):
        
        dataset=plotInputEmbed[j][1]
        lumi=plotInputEmbed[j][2]
        Xaxis=FileNamesInfo[i][1]

        MakeCompare(input+'ZTT_Tot.root', FileNamesInfo[i][0] , input+plotInputEmbed[j][0], FileNamesInfo[i][0],dataset ,lumi,Xaxis)
