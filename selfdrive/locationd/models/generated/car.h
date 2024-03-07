#pragma once
#include "rednose/helpers/ekf.h"
extern "C" {
void car_update_25(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_24(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_30(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_26(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_27(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_29(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_28(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_31(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_err_fun(double *nom_x, double *delta_x, double *out_9097705428546364050);
void car_inv_err_fun(double *nom_x, double *true_x, double *out_5952769540740002055);
void car_H_mod_fun(double *state, double *out_1702034534077900134);
void car_f_fun(double *state, double dt, double *out_3539324188133064767);
void car_F_fun(double *state, double dt, double *out_7450011976583637852);
void car_h_25(double *state, double *unused, double *out_1236988245966960864);
void car_H_25(double *state, double *unused, double *out_2734993885933809184);
void car_h_24(double *state, double *unused, double *out_5670170784642370660);
void car_H_24(double *state, double *unused, double *out_2011515441032699850);
void car_h_30(double *state, double *unused, double *out_1135489597399021944);
void car_H_30(double *state, double *unused, double *out_5253326844441057811);
void car_h_26(double *state, double *unused, double *out_6137162865059867589);
void car_H_26(double *state, double *unused, double *out_1006509432940247040);
void car_h_27(double *state, double *unused, double *out_6238661513627806509);
void car_H_27(double *state, double *unused, double *out_7476920915625001028);
void car_h_29(double *state, double *unused, double *out_8570633031827722757);
void car_H_29(double *state, double *unused, double *out_5763558188755449995);
void car_h_28(double *state, double *unused, double *out_5295151660726144074);
void car_H_28(double *state, double *unused, double *out_681159171685919421);
void car_h_31(double *state, double *unused, double *out_4918458949873699265);
void car_H_31(double *state, double *unused, double *out_2765639847810769612);
void car_predict(double *in_x, double *in_P, double *in_Q, double dt);
void car_set_mass(double x);
void car_set_rotational_inertia(double x);
void car_set_center_to_front(double x);
void car_set_center_to_rear(double x);
void car_set_stiffness_front(double x);
void car_set_stiffness_rear(double x);
}