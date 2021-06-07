# RDF plotter
import ROOT
RDF = ROOT.ROOT.RDataFrame
ROOT.ROOT.EnableImplicitMT()
import sys,os


Chain = ROOT.TChain("Events")
for path, subdirs, files in os.walk("/cms/xaastorage/NanoAOD/2017/APR20/XtoAAto4G_Signal_official/X1000A100/"):
	for name in files:
		File = os.path.join(path, name)
		if (File.endswith(".root")):
			print os.path.join(path, name)
			Chain.Add(File)
Rdf = RDF(Chain)
ROOT.gInterpreter.Declare('#include "rdf_vars.h"')
Rdf = Rdf.Define("total_weight", "9.59447/107003.")
Rdf = Rdf.Define("XM", "get_XM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4)")
Rdf = Rdf.Filter("nPhoton > 3")
Rdf = Rdf.Define("leadphotonpt","Photon_pt[0]")

H_Npho_Lazy = Rdf.Histo1D(("H_Npho", ";number of photons;events", 10, -0.5, 9.5), "nPhoton", "total_weight")
H_XM_Lazy = Rdf.Histo1D(("H_XM", ";four photon mas (GeV);events", 100, 0.,2000.), "XM", "total_weight")
H_Phopt0_Lazy = Rdf.Histo1D(("H_Phopt0", ";Leading photon pt(GeV);events", 100, 0.,2000.), "leadphotonpt", "total_weight")

H_Npho = H_Npho_Lazy.GetValue()
H_XM = H_XM_Lazy.GetValue()
H_Phopt0 = H_Phopt0_Lazy.GetValue()

C = ROOT.TCanvas()
C.cd()
H_Npho.Draw("hist")
C.SaveAs("pho.root")

C2 = ROOT.TCanvas()
C2.cd()
H_XM.Draw("e0")
C2.SaveAs("xm.root")

C3 = ROOT.TCanvas()
C3.cd()
H_Phopt0.Draw("hist")
C3.SaveAs("Phopt0.root")
