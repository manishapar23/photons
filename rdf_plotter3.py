#RDF plotter
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
ROOT.gInterpreter.Declare('#include "rdf_vars3.h"')
Rdf = Rdf.Define("total_weight", "9.59447/107003.")
Rdf = Rdf.Define("passCUT", "get_CUT(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, Photon_mvaID_WP90, 30., 2.4)")
# cut passes npho, pt, eta, phi, photon ID
CUT = "passCUT==1."
Rdf = Rdf.Filter(CUT)


# this function gets the min Mavg pairing
Rdf = Rdf.Define("AMminMpair","get_min_Mpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 0)")
Rdf = Rdf.Define("AMminMpair1","get_min_Mpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 1)")
Rdf = Rdf.Define("AMminMpair2","get_min_Mpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 2)")
Rdf = Rdf.Define("AMminMpair3","get_min_Mpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 3)")
Rdf = Rdf.Define("AMmindRpair","get_min_DRpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 0)")
Rdf = Rdf.Define("AMmindRpair1","get_min_DRpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 1)")
Rdf = Rdf.Define("AMmindRpair2","get_min_DRpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 2)")
Rdf = Rdf.Define("AMmindRpair3","get_min_DRpair(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 3)")
Rdf = Rdf.Define("XM", "get_XM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi)")
Rdf = Rdf.Define("alphaMasym", "AMminMpair/XM")
Rdf = Rdf.Define("alphadR", "AMmindRpair/XM")

H_AMMasym_Lazy = Rdf.Histo1D(("H_AMMasym", ";avg two photon mass (GeV) Masym pairing;events", 100, 0.,200.), "AMminMpair", "total_weight")
H_dR_Lazy = Rdf.Histo1D(("H_AMdR", ";avg two photon mass (GeV) dR pairing;events", 100, 0.,200.), "AMmindRpair", "total_weight")
H_XM_Lazy = Rdf.Histo1D(("H_XM", ";four photon mass (GeV);events", 100, 0.,2000.), "XM", "total_weight")
H_dRasym_Lazy = Rdf.Histo2D(("H_dRasym", "AMmindRpair vs AMminMpair", 100, 0., 200., 100, 0., 200.), "AMminMpair", "AMmindRpair", "total_weight")
H_ratioMasym_Lazy = Rdf.Histo1D(("H_ratioMasym", ";ratio of 2 photon mass (Masym) to 4 photon mass;events", 100, 0., 1.), "alphaMasym", "total_weight")
H_alpha4photon_Lazy = Rdf.Histo2D(("H_alpha4photon", "alpha (Masym) vs 4photon mass", 100, 0., 2000., 100, 0., 1.), "XM", "alphaMasym", "total_weight")
H_alphadR_Lazy = Rdf.Histo2D(("H_alphadR", "alpha (Masym) vs 2 photon mass (dR)", 100, 0., 200., 100, 0., 1.), "AMmindRpair", "alphaMasym","total_weight")
H_alphaMasym_Lazy = Rdf.Histo2D(("H_alphaMasym", "alpha (Masym) vs 2 photon mass (Masym)", 100, 0., 200., 100, 0., 1.), "AMminMpair", "alphaMasym", "total_weight")
H_42dR_Lazy = Rdf.Histo2D(("H_42dR", "4 photon mass vs 2 photon mass(dR)", 100, 0., 200., 100, 0., 2000.), "AMmindRpair", "XM", "total_weight")
H_42Masym_Lazy = Rdf.Histo2D(("H_42Masym", "4 photon mass vs 2 photon mass(Masym)", 100, 0., 200., 100, 0., 2000.), "AMminMpair", "XM", "total_weight")
H_ratiodR_Lazy = Rdf.Histo1D(("H_ratioMasym", ";ratio of 2 photon mass (dR) to 4 photon mass;events", 100, 0., 1.), "alphadR", "total_weight")
H_alpha4photon2_Lazy = Rdf.Histo2D(("H_alpha4photon2", "alpha (dR) vs 4photon mass", 100, 0., 2000., 100, 0., 1.), "XM", "alphadR", "total_weight")
H_alphadR2_Lazy =  Rdf.Histo2D(("H_alphadR2", "alpha (dR) vs 2 photon mass (dR)", 100, 0., 200., 100, 0., 1.), "AMmindRpair", "alphadR","total_weight")
H_alphaMasym2_Lazy = Rdf.Histo2D(("H_alphaMasym2", "alpha (dR) vs 2 photon mass (Masym)", 100, 0., 200., 100, 0., 1.), "AMminMpair", "alphadR", "total_weight")
H_m1m2Masym_Lazy = Rdf.Histo2D(("H_m1m2Masym", "m2 vs m1 (Masym)", 100, 0., 200., 100, 0., 200.,), "AMminMpair1", "AMminMpair2", "total_weight")
H_m1m2dR_Lazy = Rdf.Histo2D(("H_m1m2dR", "m2 vs m1 (dR)", 100, 0., 200., 100, 0., 200.,), "AMmindRpair1", "AMmindRpair2", "total_weight")
H_minMasym_Lazy = Rdf.Histo1D(("H_minMasym", ";min Mass assymetry (GeV);events", 100, 0., .1), "AMminMpair3", "total_weight")
H_mindRpair_Lazy = Rdf.Histo1D(("H_mindR", ";min dR;events", 100, 0., 10.), "AMmindRpair3", "total_weight")



H_AMMasym = H_AMMasym_Lazy.GetValue()
H_dR = H_dR_Lazy.GetValue()
H_XM = H_XM_Lazy.GetValue()
H_dRasym = H_dRasym_Lazy.GetValue()
H_ratioMasym = H_ratioMasym_Lazy.GetValue()
H_alpha4photon = H_alpha4photon_Lazy.GetValue()
H_alphadR = H_alphadR_Lazy.GetValue()
H_alphaMasym = H_alphaMasym_Lazy.GetValue()
H_42dR = H_42dR_Lazy.GetValue()
H_42Masym = H_42Masym_Lazy.GetValue()
H_ratiodR = H_ratiodR_Lazy.GetValue()
H_alpha4photon2 = H_alpha4photon2_Lazy.GetValue()
H_alphadR2 = H_alphadR2_Lazy.GetValue()
H_alphaMasym2 = H_alphaMasym2_Lazy.GetValue()
H_m1m2Masym = H_m1m2Masym_Lazy.GetValue()
H_m1m2dR = H_m1m2dR_Lazy.GetValue()
H_minMasym = H_minMasym_Lazy.GetValue()
H_mindRpair = H_mindRpair_Lazy.GetValue()

myfile = ROOT.TFile( 'test.root', 'RECREATE' )
H_AMMasym.Write()
H_dR.Write()
H_XM.Write()
H_dRasym.Write()
H_ratioMasym.Write()
H_alpha4photon.Write()
H_alphadR.Write()
H_alphaMasym.Write()
H_42dR.Write()
H_42Masym.Write()
H_ratiodR.Write()
H_alpha4photon2.Write()
H_alphadR2.Write()
H_alphaMasym2.Write()
H_m1m2Masym.Write()
H_m1m2dR.Write()
H_minMasym.Write()
H_mindRpair.Write()
