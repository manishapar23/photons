// Kinematic variables for RDF
#include <vector>
#include <stdexcept>
#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>
#include "ROOT/RVec.hxx"



using namespace ROOT::VecOps;
using rvec_f = const RVec<float> &;
using rvec_b = const RVec<bool> &;

float get_XM(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI)
        {
                  ROOT::Math::PtEtaPhiMVector v1(PT[0],ETA[0],PHI[0],M[0]);
                  ROOT::Math::PtEtaPhiMVector v2(PT[1],ETA[1],PHI[1],M[1]);
                  ROOT::Math::PtEtaPhiMVector v3(PT[2],ETA[2],PHI[2],M[2]);
                  ROOT::Math::PtEtaPhiMVector v4(PT[3],ETA[3],PHI[3],M[3]);
                  return (v1+v2+v3+v4).M();
        }	
// this function defines the cuts
float get_CUT(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI, rvec_b PID, float ptMin, float etaMin) 
        {
                if (NP > 3)
                 {
                   if (PT[3] < ptMin) return -95.;
                   if ((fabs(ETA[0]) > etaMin) or (fabs(ETA[1]) > etaMin) or (fabs(ETA[2]) > etaMin) or (fabs(ETA[3]) > etaMin)) return -90.;
                   if (PID[0]==1 && PID[1]==1 && PID[2]==1 && PID[3]==1) {
			//passed the cuts
			return 1.;
		
		   }
		} 
		return -999.;
	}

float get_min_DRpair(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI, int flag)
{

         TLorentzVector v1;
         TLorentzVector v2;
         TLorentzVector v3;
         TLorentzVector v4;
         v1.SetPtEtaPhiM(PT[0],ETA[0],PHI[0],M[0]);
         v2.SetPtEtaPhiM(PT[1],ETA[1],PHI[1],M[1]);
         v3.SetPtEtaPhiM(PT[2],ETA[2],PHI[2],M[2]);
         v4.SetPtEtaPhiM(PT[3],ETA[3],PHI[3],M[3]);

         float DR12 = v1.DeltaR(v2);
         float DR13 = v1.DeltaR(v3);
         float DR14 = v1.DeltaR(v4);
         float DR23 = v2.DeltaR(v3);
         float DR24 = v2.DeltaR(v4);
         float DR34 = v3.DeltaR(v4);
         float DeltaDR1234 = DR12 + DR34;
         float DeltaDR1324 = DR13 + DR24;
         float DeltaDR1423 = DR14 + DR23;

	 if (min({DeltaDR1234, DeltaDR1324, DeltaDR1423}) == DeltaDR1234) {
         	float am1 = (v1+v2).M();
         	float am2 = (v3+v4).M();
         	float amavg = (am1+am2)/2.;
		if (flag == 0) {
                return amavg;}
	 	if (flag == 1) {
                return am1; }
                if (flag == 2) {
                return am2;}
                if (flag == 3) {
                return DeltaDR1234;}

       } else if (min({DeltaDR1234, DeltaDR1324, DeltaDR1423}) == DeltaDR1324) {
         	float am1 = (v1+v4).M();
         	float am2 = (v2+v3).M();
         	float amavg = (am1+am2)/2.;
		if (flag == 0) {
                return amavg;}
                if (flag == 1) {
                return am1; }
                if (flag == 2) {
                return am2;}
                if (flag == 3) {
                return DeltaDR1324;}
	} 
	else if (min({DeltaDR1234, DeltaDR1324, DeltaDR1423}) == DeltaDR1423) {
		float am1 = (v1+v4).M();
         	float am2 = (v2+v3).M();
         	float amavg = (am1+am2)/2.;
		if (flag == 0) {
                return amavg;}
                if (flag == 1) {
                return am1; }
                if (flag == 2) {
                return am2;}
                if (flag == 3) {
                return DeltaDR1423;}
	}

	return -999.; 
}

// finds Masym
float Masym(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI, float m1, float m2) {
        return abs(m1 - m2) / (m1 + m2);
}


//this function gets the pairing by minimizing the Masym
float get_min_Mpair(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI, int flag) 
{
         TLorentzVector v1;
         TLorentzVector v2;
         TLorentzVector v3;
         TLorentzVector v4;
         v1.SetPtEtaPhiM(PT[0],ETA[0],PHI[0],M[0]);
         v2.SetPtEtaPhiM(PT[1],ETA[1],PHI[1],M[1]);
         v3.SetPtEtaPhiM(PT[2],ETA[2],PHI[2],M[2]);
         v4.SetPtEtaPhiM(PT[3],ETA[3],PHI[3],M[3]);

	 float M12 = (v1+v2).M();
	 float M34 = (v3+v4).M();
	 float M13 = (v1+v3).M();
	 float M24 = (v2+v4).M();
	 float M14 = (v1+v4).M();
	 float M23 = (v2+v3).M();

	 float MA1234 = Masym(NP, M, PT, ETA, PHI, M12, M34);
	 float MA1324 =  Masym(NP, M, PT, ETA, PHI, M13, M24);
	 float MA1423 =  Masym(NP, M, PT, ETA, PHI, M14, M23);


	 if (min({MA1234, MA1324, MA1423}) == MA1234) {
         	float am1 = (v1+v2).M();
         	float am2 = (v3+v4).M();
         	float amavg = (am1+am2)/2;
		if (flag == 0){
         	return amavg;}
		if (flag == 1) {
		return am1; }
		if (flag == 2) {
		return am2;}
		if (flag == 3) {
		return MA1234;}
         } else if (min({MA1234, MA1324, MA1423}) == MA1324) {
         	float am1 = (v1+v3).M();
         	float am2 = (v2+v4).M();
          	float amavg = (am1+am2)/2;
                if (flag == 0){
                return amavg;}
                if (flag == 1) {
                return am1; }
                if (flag == 2) {
                return am2;}
		if (flag == 3) {
		return MA1324; }
	 } else if (min({MA1234, MA1324, MA1423}) == MA1423) {
         	float am1 = (v1+v4).M();
         	float am2 = (v2+v3).M();
         	float amavg = (am1+am2)/2.;
                if (flag == 0){
                return amavg;}
                if (flag == 1) {
                return am1; }
                if (flag == 2) {
                return am2;}
                if (flag == 3) {
                return MA1423; }

         } 
                return -999.; // failed
}
